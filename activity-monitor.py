# @author Puji Ermanto <pujiermanto@gmail>
# @return package
import os
from pathlib import Path
import io
import subprocess
import requests
import time
import json
import sys
import platform
import pyautogui
import keyboard
from dotenv import load_dotenv
from pathlib import Path
from PySide2.QtGui import (QIcon, QPixmap)
from PySide2.QtCore import (QTimer, QTime, QEvent)
from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem, QLineEdit,
    QPushButton, QDialog, QMenu, QAction, QSystemTrayIcon, QHBoxLayout, QMessageBox
)

from PySide2.QtCore import (Qt, QDateTime)
# from pynput import keyboard, mouse
from threading import Thread
from datetime import datetime

# load_dotenv()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

load_dotenv(override=True)
# load_dotenv(resource_path('.env'))

api_url=os.getenv('API_URL')
web_url=os.getenv('WEB_URL')

print(">>> AFTER .env - API_URL =", api_url)
print("WEB_URL =", web_url)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

assets_path = resource_path("assets")
data_path = resource_path("data")

class EmailDialog(QDialog):
    def __init__(self, activity_monitor_app, parent=None):
        super().__init__(parent)
        self.activity_monitor_app = activity_monitor_app
        self.preloaded_email = None
        self.data_file = resource_path("data/activity_data.json") 
        self.setWindowTitle("Enter Email")
        self.setGeometry(300, 300, 400, 150)
        self.initUI()

    def initUI(self):
        if self.preloaded_email:
            print("Email ditemukan:", self.preloaded_email)
        else:
            print("Email belum diatur.")
            
        layout = QVBoxLayout()
        layout.setSpacing(1)
        # screen_geometry = QApplication.primaryScreen().geometry()
        # screen_width = screen_geometry.width()
        # screen_height = screen_geometry.height()
        # self.resize(screen_width, screen_height)
        
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap(resource_path("assets/logo-master.png"))
        scaled_pixmap = self.logo_pixmap.scaled(200, 100)
        self.logo_label.setPixmap(scaled_pixmap)
        self.logo_label.setFixedSize(200, 100)
        self.logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)

        self.heading_label = QLabel("Activity Monitor | PM Tokoweb", self)
        self.heading_label.setAlignment(Qt.AlignCenter)
        self.heading_label.setStyleSheet("font-size: 18px; margin-top: 5px; margin-bottom: 25px;")
        layout.addWidget(self.heading_label)

        if self.preloaded_email:
            self.user_email = self.preloaded_email
            self.accept()
        else:
            self.email_label = QLabel("Enter your active email on PM Tokoweb :")
            self.email_input = QLineEdit(self)
            self.email_input.setPlaceholderText("Email disini")
            self.email_input.setMinimumHeight(40)
            layout.addWidget(self.email_label)
            layout.addWidget(self.email_input)

        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.clicked.connect(self.confirm_email)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)
    def load_email_from_file(self):
        """Load email from the activity_data.json file if available."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    saved_email = data.get('email', '')  # Note: Ensure the correct key is used here
                    if saved_email:
                        self.user_email = saved_email
                        self.email_input.setText(self.user_email)  # Set the email in the QLineEdit
                        self.email_label.setText(f"User Email: {self.user_email}")
                        print(f"Loaded email from file: {self.user_email}")
                        return
            print("Email not found in the file, user needs to input.")
        except Exception as e:
            print(f"Error loading email from file: {e}")
            
    def confirm_email(self):
        email = self.email_input.text()
        if email:
            response = self.check_email_api(email)
            print(response)
            if response.get('status') == 'valid':
                # Ambil data user dari API untuk mendapatkan clock_in_time
                user_data = self.activity_monitor_app.get_user_data_from_api(email)
                # Pastikan user_data adalah dictionary
                print(user_data)
                if isinstance(user_data, dict):
                    attendance_data = user_data.get('data', {}).get('attendance', [])
                    print("Attendance Data:", attendance_data)
                    if attendance_data and attendance_data[0].get('in_time'):
                        # Jika clock_in_time tersedia, lanjutkan
                        self.user_email = email
                        self.accept()
                    else:
                        # Tampilkan alert jika belum clock in
                        QMessageBox.warning(self, "Clock In Required", "Silahkan , Clock In di website PM 😱")
                else:
                    QMessageBox.warning(self, "Invalid Data", "Terjadi kesalahan dalam mengambil data pengguna 🫣")
            else:
                QMessageBox.warning(self, "Invalid Data", "Email anda belum terdaftar di database PM 😱")
                self.email_label.setText("Email belum terdaftar di database PM 😱")
        else:
            QMessageBox.warning(self, "Invalid Data", "Input alamat email dengan format yang sesuai dan terdaftar di database PM 🫣")
            self.email_label.setText("Please enter a valid email 🫣")

    def check_email_api(self, email):
        """Check email validity via API"""
        try:
            response = requests.get(f'{api_url}/check-email?email={email}')
            if response.status_code == 200:
                response_data = response.json()
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
        pass
        super().__init__()
        self.setup_tray_icon()
        self.hide()  
        self.initUI()
        self.setWindowTitle("Activity Usage | PM Tokoweb")
        self.setWindowIcon(QIcon(resource_path("assets/fav-1-1.png")))
        self.start_at = None
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
            
    def start_at_next_hour(self):
        """Start the timer so that it runs at the beginning of the next hour"""
        current_time = QTime.currentTime()
        next_hour = current_time.addSecs(3600 - current_time.second() - 60 * current_time.minute())
        
        # Store the start time in the start_at property
        self.start_at = current_time.toString("yyyy-MM-dd HH:mm:ss")  # Format as per your preference
        print(f"Started at: {self.start_at}")  # For debugging

        # Menghitung waktu delay dalam milidetik
        delay = current_time.msecsTo(next_hour)

        # Mulai timer setelah delay
        QTimer.singleShot(delay, self.start_hourly_timer)

    def start_hourly_timer(self):
        """Set the timer to run every 1 hour after the initial start"""
        if self.start_at:
            # Calculate how long it has been since the start time
            start_time = QTime.fromString(self.start_at, "yyyy-MM-dd HH:mm:ss")
            current_time = QTime.currentTime()

            elapsed_time = start_time.secsTo(current_time)  # Time elapsed in seconds
            print(f"Elapsed time since start: {elapsed_time} seconds")

            # If more than 3600 seconds (1 hour), start the hourly timer
            if elapsed_time >= 3600:
                self.db_timer.start(3600000)  # 1 hour interval
                print("Starting hourly data saving.")
            else:
                # If it's still not an hour, wait for the remaining time
                delay = 3600000 - elapsed_time * 1000  # Convert to milliseconds
                QTimer.singleShot(delay, self.start_hourly_timer)
        else:
            print("start_at is not set yet.")

            
    def initUI(self):
        main_layout = QVBoxLayout()
         # self.db_timer = QTimer(self)
        # self.db_timer.timeout.connect(self.send_data_to_db)
        # self.db_timer.start(3600000)
        
        self.db_timer = QTimer(self)
        self.db_timer.timeout.connect(self.send_data_to_db)

        # Hitung interval waktu sampai jam berikutnya
        self.start_at_next_hour()
        
        screen_geometry = QApplication.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.resize(screen_width, screen_height)

        self.active_app_label = QLabel("Active Application: None")
        self.active_app_label.setStyleSheet("font-size: 14px; font-weight: bold; margin-top: 10px;")
        main_layout.addWidget(self.active_app_label)

        self.app_table = QTableWidget(0, 2)
        self.app_table.setHorizontalHeaderLabels(["Application 📝", "Usage Time 🕢"])
        self.app_table.setStyleSheet("background-color: #f7f7f7; border: 1px solid #ccc;")
        self.app_table.setColumnWidth(0, 600)
        self.app_table.setColumnWidth(1, 50)
        self.app_table.horizontalHeader().setStretchLastSection(True)
        main_layout.addWidget(self.app_table)

        self.activity_label = QLabel("Keyboard Usage 💻 : 0% | Mouse Usage 🖱️ : 0%")
        self.activity_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
        main_layout.addWidget(self.activity_label)
        
        self.device_info_label = QLabel(self.get_device_name())
        self.device_info_label.setStyleSheet("font-size: 14px; margin-top: 10px; color: gray;")
        main_layout.addWidget(self.device_info_label)

        self.email_label = QLabel("User Email: None")
        self.email_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
        main_layout.addWidget(self.email_label)
        
        self.location_label = QLabel("Location: Unknown", self)
        self.location_label.setStyleSheet("font-size: 14px; margin-top: 10px; color: gray;")
        main_layout.addWidget(self.location_label)

        self.setLayout(main_layout)
        
        self.get_location()
        
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
        
    def get_location(self):
        """Fetch user's location using ip-api.com."""
        try:
            ip_response = requests.get('https://api.ipify.org?format=json')
            ip_data = ip_response.json()
            ip_address = ip_data.get('ip')
            
            response = requests.get(f'https://ipinfo.io/{ip_address}/json')
            location = response.json()
            
            city = location.get('city', 'Unknown')
            country = location.get('country', 'Unknown')
            provider = location.get('org', 'Unknown')

            if city == 'Unknown' and country == 'Unknown':
                city = 'Unknown'
                country = 'Unknown'
                
            self.location_label.setText(f"Location: {city}, {country} | {provider}")

        except Exception as e:
            print(f"Error fetching location: {e}")



    def get_user_data_from_api(self, email):
        """Get user data from API using the provided email."""
        try:
            user_email_to_use = self.user_email if self.user_email else email
            response = requests.get(f'{api_url}/user-data?email={user_email_to_use}')
            if response.status_code == 200:
                user_data = response.json()             
                self.display_user_data(user_data)
                return user_data 
            else:
                print(f"Error fetching user data: {response.status_code}")
        except Exception as e:
            print(f"Error during fetching user data: {e}")
        return {}

    def display_user_data(self, user_data):
        """Display fetched user data in the UI."""
        user_info = user_data.get('data', {})
        if not user_info:
            print("User info is missing from the API response.")
            return
        
        # Avoid adding the same widgets multiple times
        if hasattr(self, 'clock_in_label'):
            self.clock_in_label.deleteLater()  # Remove existing widget if exists
        if hasattr(self, 'user_name_label'):
            self.user_name_label.deleteLater()
        if hasattr(self, 'user_image_label'):
            self.user_image_label.deleteLater()
        if hasattr(self, 'job_title_label'):
            self.job_title_label.deleteLater()

        attendance_data = user_info.get('attendance', [])
        if attendance_data:
            clock_in = attendance_data[0].get('in_time')
            if clock_in:
                clock_in_time = QDateTime.fromString(clock_in, "yyyy-MM-dd HH:mm:ss")
                formatted_clock_in = clock_in_time.toString("yyyy-MM-dd HH:mm:ss")
                self.clock_in_label = QLabel(f"Clock In ⌛: {formatted_clock_in} ", self)
                self.clock_in_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
                self.layout().addWidget(self.clock_in_label)
            else:
                self.clock_in_label = QLabel("Clock In: Not available", self)
                self.clock_in_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
                self.layout().addWidget(self.clock_in_label)

        first_name = user_info.get('first_name', 'Unknown')
        last_name = user_info.get('last_name', 'Unknown')
        self.user_name_label = QLabel(f"{first_name} {last_name}", self)
        self.user_name_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
        user_layout = QHBoxLayout()
        self.layout().addLayout(user_layout)

        image_path = user_info.get('image')
        if image_path:
            try:
                image_url = f'{web_url}/files/profile_images/{image_path}'
                print(f"Trying to load image from: {image_url}")
                
                response = requests.get(image_url)
                if response.status_code == 200:
                    image_data = io.BytesIO(response.content)
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data.read())
                    
                    if not pixmap.isNull():
                        self.user_image_label = QLabel(self)
                        self.user_image_label.setPixmap(pixmap)
                        self.user_image_label.setScaledContents(True)
                        self.user_image_label.setFixedSize(70, 70)
                        # user_layout.addWidget(self.user_image_label)
                        self.user_image_label.setStyleSheet("""
                            border-radius: 100%;
                            border: 2px solid #ddd;
                        """)
                        self.user_image_label.setAlignment(Qt.AlignCenter)
                        user_layout.addWidget(self.user_image_label)

                        # Add hover effect using event filter
                        self.user_image_label.installEventFilter(self)
                    else:
                        print(f"Failed to load image from response.")
                else:
                    print(f"Failed to download image, status code: {response.status_code}")
            except Exception as e:
                print(f"Error loading image: {e}")
        else:
            print("No image found in user data.")

        user_layout.addWidget(self.user_name_label)

        job_title = user_info.get('job_title', 'Not specified')
        self.job_title_label = QLabel(f"Job Title: {job_title}", self)
        self.job_title_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
        self.layout().addWidget(self.job_title_label)
        
    def eventFilter(self, obj, event):
        if obj == self.user_image_label:
            if event.type() == QEvent.HoverEnter:
                obj.setStyleSheet("""
                    border-radius: 40px;
                    border: 2px solid #ff5733;
                    transform: scale(1.1);
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                """)
            elif event.type() == QEvent.HoverLeave:
                obj.setStyleSheet("""
                    border-radius: 40px;
                    border: 2px solid #ddd;
                    transform: scale(1);
                    box-shadow: none;
                """)
        return super().eventFilter(obj, event)

            
    def show_email_dialog(self):
        """Show the email input dialog before starting activity monitoring."""
        email_dialog = EmailDialog(self)
        email_dialog.load_email_from_file()
        
        if email_dialog.exec_() == QDialog.Accepted:
            self.user_email = email_dialog.email_input.text()
            if self.user_email:
                print(f"User email set to: {self.user_email}")
                self.email_label.setText(f"User Email: {self.user_email}")
                self.get_user_data_from_api(self.user_email)
                self.start_tracking()
                return True
        return False
    
    def load_email_from_file(self):
        """Load email from the activity_data.json file if available."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    saved_email = data.get('email', '')
                    if saved_email:
                        self.preloaded_email = saved_email
                        self.user_email = saved_email  # Assign directly to user_email
                        self.email_input.setText(saved_email)  # Pre-fill the email input field
                        print(f"Loaded email from file: {self.user_email}")
                    else:
                        print("Email not found in the file, user needs to input.")
        except Exception as e:
            print(f"Error loading email from file: {e}")

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
        
    def get_active_window_title_mac(self):
        try:
            script = """
            tell application "System Events"
                set activeApp to name of first application process whose frontmost is true
            end tell
            if activeApp is "Google Chrome" then
                tell application "Google Chrome"
                    set windowTitle to title of active tab of front window
                    return windowTitle
                end tell
            else if activeApp is "Safari" then
                tell application "Safari"
                    set windowTitle to name of front document
                    return windowTitle
                end tell
            else
                return activeApp
            end if
            """
            result = subprocess.run(
                ["osascript", "-e", script],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                print(f"Error in AppleScript execution: {result.stderr}")
                return "Unknown"
            return result.stdout.strip()
        except Exception as e:
            print(f"Error getting active window title on macOS: {e}")
            return "Unknown"

        
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
                # from AppKit import NSWorkspace
                # return NSWorkspace.sharedWorkspace().activeApplication()["NSApplicationName"]
                return get_active_window_title_mac()
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
            time_item = QTableWidgetItem(f"{h}h {m}m {s}s")
            # For mac 
            # time_item.setTextAlignment(0x0004)
            time_item.setTextAlignment(Qt.AlignCenter)
            self.app_table.setItem(row, 1, time_item)

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
        if not self.user_email:  # Prevent saving if the email is not set
            return

        device_name = self.get_device_name() 
        location = self.location_label.text().replace("Location: ", "") if hasattr(self, 'location_label') else "Location not available"
        
        data = {
            'email': self.user_email,
            "location": location,
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
    def send_data_to_db(self, total_work_seconds, elapsed_time_ratio):
        """Send data stored in JSON file to the database."""
        if os.path.exists(self.data_file):
            
            with open(self.data_file, 'r') as json_file:
                data = json.load(json_file)

            payload = {
                'email': data['email'],
                "location": data['location'],
                'app_usage_time': json.dumps(data['app_usage_time']),
                # 'app_usage_time': data['app_usage_time'],
                'keyboard_usage': data['keyboard_usage'],
                'mouse_usage': data['mouse_usage'],
                'device': data['device'],
                'created_at': data['created_at']
            }
            
            url = f'{api_url}/send-activity'
            try:
                response = requests.post(url, data=payload)
                if response.status_code == 200:
                    print("Data berhasil dikirim ke database")
                else:
                    print(f"Terjadi kesalahan saat mengirim data: {response.status_code}")
            except Exception as e:
                print(f"Error saat mengirim data ke API: {e}")
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
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ActivityMonitorApp()
    window.show()
    sys.exit(app.exec_())