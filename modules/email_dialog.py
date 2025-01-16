import requests
from PySide2.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
from utils import resource_path

class EmailDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.email_input = QLineEdit(self)
        self.setWindowTitle("Enter Email")
        self.setGeometry(300, 300, 400, 150)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.logo_label = QLabel(self)
        logo_pixmap = QPixmap(resource_path("assets/logo-master.png"))
        self.logo_label.setPixmap(logo_pixmap.scaled(200, 100))
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)

        self.email_label = QLabel("Enter your active email on PM Tokoweb:")
        layout.addWidget(self.email_label)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
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
                self.email_label.setText("Email not registered in database.")
        else:
            self.email_label.setText("Please enter a valid email.")

    def check_email_api(self, email):
        try:
            response = requests.get(f'https://pm-activity.tokoweb.live/api/check-email?email={email}')
            if response.status_code == 200:
                return {'status': 'valid'} if response.json().get('status') else {'status': 'invalid'}
        except Exception:
            pass
        return {'status': 'invalid'}
