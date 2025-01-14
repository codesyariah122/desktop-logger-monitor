import requests
import json
import sys
import platform
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QDialog
from pynput import keyboard, mouse
from pynput.mouse import Listener as MouseListener
from threading import Thread
import os
from datetime import datetime
from threading import Thread

class EmailDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Email")
        self.setGeometry(300, 300, 400, 150)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        self.email_label = QLabel("Enter your email:")
        layout.addWidget(self.email_label)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.clicked.connect(self.confirm_email)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def confirm_email(self):
        email = self.email_input.text().strip()
        if email and "@" in email:  # Periksa email valid
            self.accept()
        else:
            self.email_label.setText("Please enter a valid email.")

class ActivityMonitorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_usage)
        self.timer.start(1000)
        self.current_active_window = ""
        self.app_usage_time = {}
        self.total_keyboard_events = 0
        self.total_mouse_events = 0
        self.total_time_seconds = 0
        self.user_email = ""
        self.work_start_time = None
        self.data_file = "activity_data.json" 
        self.show_email_dialog()
        self.elapsed_time = 0

    def initUI(self):
        main_layout = QVBoxLayout()

        self.active_app_label = QLabel("Active Application: None")
        self.active_app_label.setStyleSheet("font-size: 14px; font-weight: bold; margin-top: 10px;")
        main_layout.addWidget(self.active_app_label)

        self.app_table = QTableWidget(0, 2)
        self.app_table.setHorizontalHeaderLabels(["Application", "Usage Time"])
        self.app_table.setStyleSheet("background-color: #f7f7f7; border: 1px solid #ccc;")
        self.app_table.horizontalHeader().setStretchLastSection(True)
        main_layout.addWidget(self.app_table)

        self.activity_label = QLabel("Keyboard Usage: 0%, Mouse Usage: 0%")
        self.activity_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
        main_layout.addWidget(self.activity_label)

        self.email_label = QLabel("User Email: None")
        self.email_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
        main_layout.addWidget(self.email_label)

        self.setLayout(main_layout)

    def show_email_dialog(self):
        """Show the email input dialog before starting activity monitoring."""
        email_dialog = EmailDialog()
        if email_dialog.exec_() == QDialog.Accepted:
            self.user_email = email_dialog.email_input.text()
            print(f"User email set to: {self.user_email}")
            self.email_label.setText(f"User Email: {self.user_email}")  # Update the email label
            self.start_tracking()  # Start monitoring once email is confirmed

    def start_tracking(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_keyboard_event)
        keyboard_thread = Thread(target=keyboard_listener.start)
        keyboard_thread.daemon = True
        keyboard_thread.start()

        mouse_listener = MouseListener(on_click=self.on_mouse_event, on_move=self.on_mouse_move)
        mouse_thread = Thread(target=mouse_listener.start)
        mouse_thread.daemon = True
        mouse_thread.start()

    def on_keyboard_event(self, key):
        self.total_keyboard_events += 1

    def on_mouse_event(self, x, y, button, pressed):
        if pressed:
            self.total_mouse_events += 1
            print(f"Mouse clicked. Total mouse events: {self.total_mouse_events}")

    def on_mouse_move(self, x, y):
        self.total_mouse_events += 1
        print(f"Mouse moved. Total mouse events: {self.total_mouse_events}")

    def get_active_window(self):
        """Dapatkan nama jendela aplikasi aktif"""
        try:
            if platform.system() == "Windows":
                import win32gui
                window = win32gui.GetForegroundWindow()
                return win32gui.GetWindowText(window)
            elif platform.system() == "Linux":
                import subprocess
                output = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"])
                return output.decode("utf-8").strip()
            elif platform.system() == "Darwin":
                from AppKit import NSWorkspace
                return NSWorkspace.sharedWorkspace().activeApplication()["NSApplicationName"]
        except Exception as e:
            print(f"Error detecting active window: {e}")
        return "Unknown"
    
    def update_usage(self):
        active_window = self.get_active_window()
        if active_window and active_window != self.current_active_window:
            self.current_active_window = active_window
            if active_window not in self.app_usage_time:
                self.app_usage_time[active_window] = 0

        if self.current_active_window in self.app_usage_time:
            self.app_usage_time[self.current_active_window] += 1

        self.active_app_label.setText(f"Active Application: {self.current_active_window}")

        self.app_table.setRowCount(len(self.app_usage_time))
        for row, (app, time_used) in enumerate(self.app_usage_time.items()):
            h, m, s = self.format_time(time_used)
            self.app_table.setItem(row, 0, QTableWidgetItem(app))
            self.app_table.setItem(row, 1, QTableWidgetItem(f"{h}h {m}m {s}s"))

        self.total_time_seconds += 1

        total_work_seconds = 8 * 3600
        elapsed_time_ratio = self.total_time_seconds / total_work_seconds
        self.elapsed_time = elapsed_time_ratio

        keyboard_usage = (self.total_keyboard_events / total_work_seconds) * 100 * elapsed_time_ratio
        mouse_usage = (self.total_mouse_events / total_work_seconds) * 100 * elapsed_time_ratio

        self.activity_label.setText(f"Keyboard Usage: {keyboard_usage:.2f}%, Mouse Usage: {mouse_usage:.2f}%")

        # Save data to JSON file
        self.save_data_to_json()


    def format_time(self, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return int(hours), int(minutes), int(seconds)

    def save_data_to_json(self):
        """Simpan data ke file JSON."""
        total_work_time_seconds = 8 * 3600
        elapsed_time = min(self.total_time_seconds, total_work_time_seconds)

        keyboard_usage = self.total_keyboard_events / total_work_time_seconds if elapsed_time > 0 else 0
        mouse_usage = self.total_mouse_events / total_work_time_seconds if elapsed_time > 0 else 0

        data = {
            'email': self.user_email,
            'app_usage_time': self.app_usage_time,
            'keyboard_usage': keyboard_usage,
            'mouse_usage': mouse_usage,
            'created_at': str(datetime.now())
        }

        with open(self.data_file, 'w') as json_file:
            json.dump(data, json_file)

    def closeEvent(self, event):
        """Called when the application is closed."""
        # Send data to database before closing
        self.send_data_to_db()
        event.accept()

    def send_data_to_db(self):
        """Kirim data ke database."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as json_file:
                data = json.load(json_file)

            # Periksa apakah semua field di payload ada dan valid
            if not data.get('email') or not data.get('app_usage_time'):
                print("Error: Data tidak lengkap, tidak bisa mengirim ke database.")
                return

            data['keyboard_usage'] = round(data['keyboard_usage'] * 100, 2)
            data['mouse_usage'] = round(data['mouse_usage'] * 100, 2)

            payload = {
                'email': data['email'],
                'app_usage_time': json.dumps(data['app_usage_time']),  # JSON-stringify dictionary
                'keyboard_usage': data['keyboard_usage'],
                'mouse_usage': data['mouse_usage'],
                'created_at': data['created_at']
            }

            url = 'http://localhost:9091/send-activity'
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    print("Data berhasil dikirim ke database:", payload)
                else:
                    print(f"Terjadi kesalahan saat mengirim data: {response.status_code}, Response: {response.text}")
            except Exception as e:
                print(f"Error saat mengirim data ke API: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ActivityMonitorApp()
    window.show()
    sys.exit(app.exec_())
