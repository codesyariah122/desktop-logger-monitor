# @author Puji Ermanto <pujiermanto@gmail>
# @return package

import os
import io
import requests
import time
import json
import sys
import platform
import pyautogui
import keyboard
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem, QLineEdit,
    QPushButton, QDialog, QMenu, QAction, QSystemTrayIcon
)

from PySide2.QtCore import Qt
# from pynput import keyboard, mouse
from PySide2.QtWidgets import QSystemTrayIcon,  QMenu, QAction
from threading import Thread
from datetime import datetime

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
        
        layout.setSpacing(1)
        
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap(resource_path("assets/logo-master.png"))
        scaled_pixmap = self.logo_pixmap.scaled(200, 100)
        self.logo_label.setPixmap(scaled_pixmap)
        self.logo_label.setFixedSize(200, 100)
        self.logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.logo_label)

        self.heading_label = QLabel("Activity Monitor | PM Tokoweb", self)
        self.heading_label.setAlignment(Qt.AlignCenter)
        self.heading_label.setStyleSheet("font-size: 18px; margin-bottom: 20px;")
        layout.addWidget(self.heading_label)

        self.email_label = QLabel("Enter your active email on PM Tokoweb :")
        layout.addWidget(self.email_label)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setMinimumHeight(40)
        layout.addWidget(self.email_input)

        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.clicked.connect(self.confirm_email)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)
    def confirm_email(self):
        email = self.email_input.text()
        if email:
            response = self.check_email_api(email)
            if response.get('status') == 'valid':
                self.user_email = email
                self.accept()
            else:
                self.email_label.setText("Email belum terdaftar di database PM.")
        else:
            self.email_label.setText("Please enter a valid email.")

    def check_email_api(self, email):
        """Check email validity via API"""
        try:
            response = requests.get(f'https://pm-activity.tokoweb.live/api/check-email?email={email}')
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
        self.setup_tray_icon()
        self.hide()  
        self.initUI()
        self.setWindowTitle("Activity Usage | PM Tokoweb")
        self.setWindowIcon(QIcon(resource_path("assets/fav-1-1.png")))
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

        if not self.show_email_dialog():
            sys.exit(0)
    def setup_tray_icon(self):
        icon_path = resource_path("assets/fav-1-1.webp")
        icon = QIcon(icon_path)
        
        self.tray_icon = QSystemTrayIcon(icon, self)
        self.tray_icon.setToolTip("Activity Monitor PM Tokoweb is Running")
        
        tray_menu = QMenu()
        
        show_action = QAction("Show Application", self)
        show_action.triggered.connect(self.show)
        tray_menu.addAction(show_action)
        
        hide_action = QAction("Hide Application", self)
        hide_action.triggered.connect(self.hide)
        tray_menu.addAction(hide_action)
        
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.quit_application)
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
        self.tray_icon.activated.connect(self.on_tray_icon_activated)

        
    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show()

    def quit_application(self):
        QApplication.quit()
        
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

        self.activity_label = QLabel("Keyboard Usage: 0% | Mouse Usage: 0%")
        self.activity_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
        main_layout.addWidget(self.activity_label)

        self.email_label = QLabel("User Email: None")
        self.email_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
        main_layout.addWidget(self.email_label)
        
        self.device_info_label = QLabel(self.get_device_name())
        self.device_info_label.setStyleSheet("font-size: 14px; margin-top: 10px; color: gray;")
        main_layout.addWidget(self.device_info_label)
        
        self.db_timer = QTimer(self)
        self.db_timer.timeout.connect(self.send_data_to_db)
        self.db_timer.start(3600000)

        self.setLayout(main_layout)

    def get_user_data_from_api(self):
        """Get user data from API using the provided email."""
        try:
            response = requests.get(f'https://pm-activity.tokoweb.live/api/user-data?email={self.user_email}')
            if response.status_code == 200:
                user_data = response.json()             
                self.display_user_data(user_data)
            else:
                print(f"Error fetching user data: {response.status_code}")
        except Exception as e:
            print(f"Error during fetching user data: {e}")

    def display_user_data(self, user_data):
        """Display fetched user data in the UI."""        
        user_info = user_data.get('data', {})
        if not user_info:
            print("User info is missing from the API response.")
            return

        first_name = user_info.get('first_name', 'Unknown')
        last_name = user_info.get('last_name', 'Unknown')
        self.user_name_label = QLabel(f"Name: {first_name} {last_name}", self)
        self.user_name_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
        self.layout().addWidget(self.user_name_label)

        job_title = user_info.get('job_title', 'Not specified')
        self.job_title_label = QLabel(f"Job Title: {job_title}", self)
        self.job_title_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
        self.layout().addWidget(self.job_title_label)

        image_path = user_info.get('image')
        
        if image_path:
            try:
                image_url = f'https://pm.tokoweb.live/files/profile_images/{image_path}'
                print(f"Trying to load image from: {image_url}")
                
                response = requests.get(image_url)
                if response.status_code == 200:
                    image_data = io.BytesIO(response.content)
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data.read())
                    
                    if not pixmap.isNull():  # Ensure the image is valid
                        self.user_image_label = QLabel(self)
                        self.user_image_label.setPixmap(pixmap)
                        self.user_image_label.setScaledContents(True)
                        self.user_image_label.setFixedSize(100, 100)
                        self.layout().addWidget(self.user_image_label)
                    else:
                        print(f"Failed to load image from response.")
                else:
                    print(f"Failed to download image, status code: {response.status_code}")
            except Exception as e:
                print(f"Error loading image: {e}")
        else:
            print("No image found in user data.")
            
    def show_email_dialog(self):
        """Show the email input dialog before starting activity monitoring."""
        email_dialog = EmailDialog()
        if email_dialog.exec_() == QDialog.Accepted:
            self.user_email = email_dialog.email_input.text()
            if self.user_email:
                print(f"User email set to: {self.user_email}")
                self.email_label.setText(f"User Email: {self.user_email}")
                self.get_user_data_from_api()
                self.start_tracking()
                return True
        return False
    def start_tracking(self):
        keyboard_thread = Thread(target=self.monitor_keyboard_events)
        keyboard_thread.start()
        mouse_thread = Thread(target=self.monitor_mouse_events)
        mouse_thread.start()

    def monitor_keyboard_events(self):
        while True:
            event = keyboard.read_event()
            if event.event_type == "down":  # Key press event
                self.total_keyboard_events += 1
                print(f"Key pressed: {event.name}")
   
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

        self.activity_label.setText(f"Keyboard Usage: {self.keyboard_usage:.2f}% | Mouse Usage: {self.mouse_usage:.2f}%")

        self.save_data_to_json()

    def format_time(self, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return int(hours), int(minutes), int(seconds)
    
    def get_device_name(self):
        system_info = platform.system()
        node_name = platform.node()
        machine_type = platform.machine()
        processor_type = platform.processor()

        return f"Device: {node_name}, System: {system_info}, Processor: {processor_type}, Architecture: {machine_type}"

    def save_data_to_json(self):
        """Save the usage data to a JSON file."""
        device_name = self.get_device_name() 
        
        data = {
            'email': self.user_email,
            'app_usage_time': self.app_usage_time,
            'keyboard_usage': self.keyboard_usage,
            'mouse_usage': self.mouse_usage,
            "device": device_name,
            'created_at': str(datetime.now())
        }

        try:
            with open(self.data_file, 'w') as json_file:
                json.dump(data, json_file)
        except Exception as e:
            print(f"Error saving data to JSON: {e}")

    def get_elapsed_time_ratio(self, total_work_seconds):
        """Menghitung rasio waktu yang telah berlalu."""
        elapsed_time = time.time() - self.start_time
        return elapsed_time / total_work_seconds if total_work_seconds > 0 else 0
    
    def quit_application(self):
        """Handle the quit action, send data before quitting."""
        total_work_seconds = 3600
        elapsed_time_ratio = self.get_elapsed_time_ratio(total_work_seconds)
        self.send_data_to_db(total_work_seconds, elapsed_time_ratio)
        
        self.tray_icon.hide()
        
        QApplication.quit()
        sys.exit() 
    
    def closeEvent(self, event):
        """Override closeEvent to minimize the app to the system tray instead of exiting."""
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "Minimized to Tray",
            "The application is still running in the system tray. Double-click the icon to restore it.",
            QSystemTrayIcon.Information,
            3000
        )

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
                'device': data['device'],
                'created_at': data['created_at']
            }

            url = 'https://pm-activity.tokoweb.live/api/send-activity'
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

