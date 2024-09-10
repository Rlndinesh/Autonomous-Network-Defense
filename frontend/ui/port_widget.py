from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
import requests

class PortWidget(QWidget):
    def __init__(self, parent=None):
        super(PortWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.port_label = QLabel("Open Ports:")
        self.port_list = QListWidget()
        self.btn_fetch_ports = QPushButton("Fetch Open Ports")
        self.btn_fetch_ports.clicked.connect(self.fetch_ports)

        layout = QVBoxLayout()
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_list)
        layout.addWidget(self.btn_fetch_ports)
        self.setLayout(layout)

    def fetch_ports(self):
        response = requests.get('http://localhost:5000/network/ports')
        if response.status_code == 200:
            ports = response.json()
            self.port_list.clear()
            for port in ports:
                self.port_list.addItem(f"Port {port} is open")
