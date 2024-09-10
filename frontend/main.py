# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from ui.traffic_widget import TrafficWidget
# from ui.blocked_widget import BlockedWidget

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Autonomous Network Defense System')
#         self.setGeometry(200, 200, 500, 400)

#         layout = QVBoxLayout()

#         self.traffic_widget = TrafficWidget()
#         self.blocked_widget = BlockedWidget()

#         layout.addWidget(self.traffic_widget)
#         layout.addWidget(self.blocked_widget)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())




#  v1

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from ui.traffic_widget import TrafficWidget
from ui.port_widget import PortWidget

class DefenseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Autonomous Network Defense System")

        # Instantiate UI components
        self.traffic_widget = TrafficWidget()
        self.port_widget = PortWidget()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.traffic_widget)
        layout.addWidget(self.port_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DefenseApp()
    window.show()
    sys.exit(app.exec_())




# import sys
# import requests
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QListWidget

# class DefenseApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("Autonomous Network Defense System")

#         # Network Traffic Button
#         self.traffic_label = QLabel("Network Traffic:")
#         self.traffic_list = QListWidget()
#         self.btn_fetch_traffic = QPushButton("Fetch Traffic")
#         self.btn_fetch_traffic.clicked.connect(self.fetch_traffic)

#         # Open Ports Button
#         self.port_label = QLabel("Open Ports:")
#         self.port_list = QListWidget()
#         self.btn_fetch_ports = QPushButton("Fetch Open Ports")
#         self.btn_fetch_ports.clicked.connect(self.fetch_ports)

#         # Layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.traffic_label)
#         layout.addWidget(self.traffic_list)
#         layout.addWidget(self.btn_fetch_traffic)
#         layout.addWidget(self.port_label)
#         layout.addWidget(self.port_list)
#         layout.addWidget(self.btn_fetch_ports)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def fetch_traffic(self):
#         response = requests.get('http://localhost:5000/network/traffic')
#         if response.status_code == 200:
#             traffic = response.json()
#             self.traffic_list.clear()
#             for packet in traffic:
#                 self.traffic_list.addItem(str(packet))

#     def fetch_ports(self):
#         response = requests.get('http://localhost:5000/network/ports')
#         if response.status_code == 200:
#             ports = response.json()
#             self.port_list.clear()
#             for port in ports:
#                 self.port_list.addItem(f"Port {port} is open")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = DefenseApp()
#     window.show()
#     sys.exit(app.exec_())
