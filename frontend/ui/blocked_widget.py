import requests
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QMessageBox

class BlockedWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.blocked_list = QListWidget()
        self.fetch_button = QPushButton('Fetch Blocked Traffic')
        self.fetch_button.clicked.connect(self.fetch_blocked_traffic)

        layout.addWidget(QLabel('Blocked Traffic:'))
        layout.addWidget(self.blocked_list)
        layout.addWidget(self.fetch_button)

        self.setLayout(layout)

    def fetch_blocked_traffic(self):
        try:
            response = requests.get('http://localhost:5000/network/blocked')
            response.raise_for_status()
            blocked_data = response.json()

            self.blocked_list.clear()
            for blocked in blocked_data:
                self.blocked_list.addItem(f"Blocked IP: {blocked}")

        except requests.exceptions.RequestException as e:
            error_msg = QMessageBox()
            error_msg.setIcon(QMessageBox.Critical)
            error_msg.setText(f"Error fetching blocked traffic: {e}")
            error_msg.setWindowTitle("Network Error")
            error_msg.exec_()
