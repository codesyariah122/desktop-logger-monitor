import os
import logging
import requests
import time
import json
import sys
import platform
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QDialog, QHBoxLayout
# from pynput import keyboard, mouse
import pyautogui
import keyboard
from threading import Thread
from datetime import datetime

# logging.basicConfig(level=logging.DEBUG, filename="app_debug.log")
# logging.debug("Debugging log started")

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

assets_path = resource_path("assets")
data_path = resource_path("data")

class EmailDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Email")
        self.setGeometry(300, 300, 400, 150)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.email_label = QLabel("Enter email on active email PM Tokoweb :")
        layout.addWidget(self.email_label)

        email_layout = QVBoxLayout()

        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap(resource_path("assets/logo-master.png"))
        scaled_pixmap = self.logo_pixmap.scaled(100, 60)
        self.logo_label.setPixmap(scaled_pixmap)
        self.logo_label.setFixedSize(100, 60)
        email_layout.addWidget(self.logo_label)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setMinimumHeight(40)
        email_layout.addWidget(self.email_input)

        layout.addLayout(email_layout)

        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.clicked.connect(self.confirm_email)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def confirm_email(self):
        email = self.email_input.text()

        if email:
            response = self.check_email_api(email)
            
            if response.get('status') == 'valid':
                self.accept()
            else:
                self.email_label.setText("Email belum terdaftar di database PM.")
        else:
            self.email_label.setText("Please enter a valid email.")

    def check_email_api(self, email):
        """Check email validity via API"""
        try:
            response = requests.get(f'http://localhost:9091/api/check-email?email={email}')
            if response.status_code == 200:
                response_data = response.json()
                print("API Response:", response_data)
                if response_data.get('status') == True:
                    return {'status': 'valid'}
                else:
                    return {'status': 'invalid', 'message': response_data.get('message', 'Email is invalid')}
            else:
                print(f"Error checking email: {response.status_code}")
        except Exception as e:
            print(f"Error during email check: {e}")
        return {'status': 'invalid', 'message': 'Error during email check'}
    
class ActivityMonitorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Activity Usage | PM Tokoweb")
        self.setWindowIcon(QIcon(resource_path("assets/fav-1-1.webp")))
        self.last_mouse_position = None
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
        self.data_file = resource_path("data/activity_data.json")
        self.elapsed_time = 0
        self.start_time = 0
        self.keyboard_usage = 0
        self.mouse_usage = 0
        self.timer.start(100)

        # Show email dialog and check if user input is valid
        if not self.show_email_dialog():
            sys.exit(0)  # If email is not provided, exit the program

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
            if self.user_email:  # Only proceed if a valid email is entered
                print(f"User email set to: {self.user_email}")
                self.email_label.setText(f"User Email: {self.user_email}")  # Update the email label
                self.start_tracking()  # Start monitoring once email is confirmed
                return True
        return False  # Return False if the dialog was closed or email was invalid

    def start_tracking(self):
        # keyboard_listener = keyboard.Listener(on_press=self.on_keyboard_event)
        # keyboard_thread = Thread(target=keyboard_listener.start)
        # keyboard_thread.start()

        # mouse_listener = mouse.Listener(on_click=self.on_mouse_event, on_move=self.on_mouse_move)
        # mouse_thread = Thread(target=mouse_listener.start)
        # mouse_thread.start()
        
        # keyboard_thread.join()
        # mouse_thread.join()
        # keyboard_listener = keyboard.Listener(on_press=self.on_keyboard_event)
        # keyboard_listener.start() 

        # mouse_listener = mouse.Listener(on_click=self.on_mouse_event, on_move=self.on_mouse_move)
        # mouse_listener.start()
        
        # New rules code
        keyboard_thread = Thread(target=self.monitor_keyboard_events)
        keyboard_thread.start()
        # Mouse listener tetap menggunakan pynput
        mouse_thread = Thread(target=self.monitor_mouse_events)
        mouse_thread.start()

    # def on_keyboard_event(self, key):
    #     self.total_keyboard_events += 1
    def monitor_keyboard_events(self):
        while True:
            event = keyboard.read_event()
            if event.event_type == "down":  # Key press event
                self.total_keyboard_events += 1
                print(f"Key pressed: {event.name}")
                
    # def on_keyboard_event(key):
    #     try:
    #         print(f"Key pressed: {key.char}")
    #     except AttributeError:
    #         print(f"Special key pressed: {key}")
    # keyboard_listener = keyboard.Listener(on_press=on_keyboard_event)
    # keyboard_listener.start()

    # def on_mouse_event(self, x, y, button, pressed):  
    #     if pressed:
    #         self.total_mouse_events += 1
    #         print(f"Mouse clicked at ({x}, {y}) with button {button}")
    # def on_mouse_event(x, y, button, pressed):
    #     if pressed:
    #         print(f"Mouse clicked at ({x}, {y}) with {button}")
    # mouse_listener = mouse.Listener(on_click=on_mouse_event)
    # mouse_listener.start()
    
    def monitor_mouse_events(self):
        while True:
            current_position = pyautogui.position()
            if self.last_mouse_position is not None and current_position != self.last_mouse_position:
                self.total_mouse_events += 1
            self.last_mouse_position = current_position
            time.sleep(0.1)


    def on_mouse_move(self, x, y):
        self.total_mouse_events += 1

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

        self.keyboard_usage = (self.total_keyboard_events / total_work_seconds) * 100 * elapsed_time_ratio
        self.mouse_usage = (self.total_mouse_events / total_work_seconds) * 100 * elapsed_time_ratio

        self.activity_label.setText(f"Keyboard Usage: {self.keyboard_usage:.2f}%, Mouse Usage: {self.mouse_usage:.2f}%")

        self.save_data_to_json()

    def format_time(self, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return int(hours), int(minutes), int(seconds)

    def save_data_to_json(self):
        """Save the usage data to a JSON file."""
        data = {
            'email': self.user_email,
            'app_usage_time': self.app_usage_time,
            'keyboard_usage': self.keyboard_usage,
            'mouse_usage': self.mouse_usage,
            'created_at': str(datetime.now())
        }

        with open(self.data_file, 'w') as json_file:
            json.dump(data, json_file)

    def get_elapsed_time_ratio(self, total_work_seconds):
        """Menghitung rasio waktu yang telah berlalu."""
        elapsed_time = time.time() - self.start_time
        return elapsed_time / total_work_seconds if total_work_seconds > 0 else 0
    
    def closeEvent(self, event):
        """Called when the application is closed."""
        total_work_seconds = 3600
        elapsed_time_ratio = self.get_elapsed_time_ratio(total_work_seconds)
        self.send_data_to_db(total_work_seconds, elapsed_time_ratio)
        event.accept()

    def send_data_to_db(self, total_work_seconds, elapsed_time_ratio):
        """Send data stored in JSON file to the database."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as json_file:
                data = json.load(json_file)

            payload = {
                'email': data['email'],
                'app_usage_time': json.dumps(data['app_usage_time']),
                'keyboard_usage': data['keyboard_usage'],
                'mouse_usage': data['mouse_usage'],
                'created_at': data['created_at']
            }

            url = 'http://localhost:9091/api/send-activity'
            try:
                response = requests.post(url, data=payload)
                if response.status_code == 200:
                    print("Data berhasil dikirim ke database")
                else:
                    print(f"Terjadi kesalahan saat mengirim data: {response.status_code}")
            except Exception as e:
                print(f"Error saat mengirim data ke API: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ActivityMonitorApp()
    window.show()
    sys.exit(app.exec_())

