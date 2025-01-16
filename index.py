import sys
from PySide2.QtWidgets import QApplication
from modules.email_dialog import EmailDialog
from modules.activity_monitor_app import ActivityMonitorApp

if __name__ == "__main__":
    app = QApplication(sys.argv)

    email_dialog = EmailDialog()
    if email_dialog.exec_():
        user_email = email_dialog.email_input.text()
        monitor_app = ActivityMonitorApp(user_email)
        monitor_app.show()

    sys.exit(app.exec_())
