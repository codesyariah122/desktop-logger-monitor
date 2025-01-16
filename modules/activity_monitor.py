from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QMenu, QAction, QSystemTrayIcon
from PySide2.QtGui import QIcon
from PySide2.QtCore import QTimer
from utils import resource_path
from threading import Thread
import time
import pyautogui
import keyboard

class ActivityMonitorApp(QWidget):
    def __init__(self, user_email):
        super().__init__()
        self.user_email = user_email
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Activity Usage | PM Tokoweb")
        self.setWindowIcon(QIcon(resource_path("assets/fav-1-1.png")))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_usage)
        self.timer.start(1000)

        layout = QVBoxLayout()
        self.active_app_label = QLabel("Active Application: None")
        layout.addWidget(self.active_app_label)

        self.app_table = QTableWidget(0, 2)
        self.app_table.setHorizontalHeaderLabels(["Application", "Usage Time"])
        layout.addWidget(self.app_table)

        self.setLayout(layout)
        self.start_tracking()

    def start_tracking(self):
        keyboard_thread = Thread(target=self.monitor_keyboard_events)
        keyboard_thread.start()
        mouse_thread = Thread(target=self.monitor_mouse_events)
        mouse_thread.start()

    def monitor_keyboard_events(self):
        while True:
            keyboard.read_event()
            print("Keyboard event detected.")

    def monitor_mouse_events(self):
        while True:
            pyautogui.position()
            time.sleep(0.1)

    def update_usage(self):
        print("Updating usage...")
