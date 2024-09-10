# import requests
# from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QMessageBox

# class TrafficWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()

#         self.traffic_list = QListWidget()
#         self.fetch_button = QPushButton('Fetch Traffic')
#         self.fetch_button.clicked.connect(self.fetch_traffic)

#         layout.addWidget(QLabel('Network Traffic:'))
#         layout.addWidget(self.traffic_list)
#         layout.addWidget(self.fetch_button)

#         self.setLayout(layout)

#     def fetch_traffic(self):
#         try:
#             response = requests.get('http://localhost:5000/network/traffic')
#             response.raise_for_status()
#             traffic_data = response.json()

#             self.traffic_list.clear()
#             for packet in traffic_data:
#                 self.traffic_list.addItem(f"Src: {packet['source_ip']} -> Dst: {packet['destination_ip']} ({packet['protocol']})")

#         except requests.exceptions.RequestException as e:
#             error_msg = QMessageBox()
#             error_msg.setIcon(QMessageBox.Critical)
#             error_msg.setText(f"Error fetching network traffic: {e}")
#             error_msg.setWindowTitle("Network Error")
#             error_msg.exec_()



# v1

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
import requests


class TrafficWidget(QWidget):
    def __init__(self, parent=None):
        super(TrafficWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # Network Traffic Section
        self.traffic_label = QLabel("Network Traffic:")
        self.traffic_list = QListWidget()
        self.btn_fetch_traffic = QPushButton("Fetch Traffic")
        self.btn_fetch_traffic.clicked.connect(self.fetch_traffic)

        # Blocked Traffic Section
        self.blocked_label = QLabel("Blocked Traffic:")
        self.blocked_list = QListWidget()
        self.btn_fetch_blocked = QPushButton("Fetch Blocked Traffic")
        self.btn_fetch_blocked.clicked.connect(self.fetch_blocked_traffic)

        layout = QVBoxLayout()
        layout.addWidget(self.traffic_label)
        layout.addWidget(self.traffic_list)
        layout.addWidget(self.btn_fetch_traffic)
        layout.addWidget(self.blocked_label)
        layout.addWidget(self.blocked_list)
        layout.addWidget(self.btn_fetch_blocked)
        self.setLayout(layout)

    def fetch_traffic(self):
        response = requests.get('http://localhost:5000/network/traffic')
        if response.status_code == 200:
            traffic = response.json()
            self.traffic_list.clear()
            for packet in traffic:
                self.traffic_list.addItem(str(packet))
        
    def fetch_blocked_traffic(self):
        response = requests.get('http://localhost:5000/network/blocked')
        if response.status_code == 200:
            blocked_traffic = response.json()
            self.blocked_list.clear()
            for blocked_event in blocked_traffic:
                self.blocked_list.addItem(blocked_event)


# from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
# import requests

# class TrafficWidget(QWidget):
#     def __init__(self, parent=None):
#         super(TrafficWidget, self).__init__(parent)
#         self.initUI()

#     def initUI(self):
#         self.traffic_label = QLabel("Network Traffic:")
#         self.traffic_list = QListWidget()
#         self.btn_fetch_traffic = QPushButton("Fetch Traffic")
#         self.btn_fetch_traffic.clicked.connect(self.fetch_traffic)

#         layout = QVBoxLayout()
#         layout.addWidget(self.traffic_label)
#         layout.addWidget(self.traffic_list)
#         layout.addWidget(self.btn_fetch_traffic)
#         self.setLayout(layout)

#     def fetch_traffic(self):
#         response = requests.get('http://localhost:5000/network/traffic')
#         if response.status_code == 200:
#             traffic = response.json()
#             self.traffic_list.clear()
#             for packet in traffic:
#                 self.traffic_list.addItem(str(packet))
