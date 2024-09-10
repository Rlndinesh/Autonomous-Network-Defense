import random

# Function to capture network traffic
def capture_network_traffic():
    # Simulated traffic packets
    return [{'source_ip': '192.168.1.101', 'destination_ip': '8.8.8.8', 'protocol': 'TCP'},
            {'source_ip': '192.168.1.102', 'destination_ip': '8.8.4.4', 'protocol': 'UDP'}]

# Function to detect anomalies in traffic
def detect_anomalies():
    # Simulated anomaly detection (e.g., ARP spoofing)
    return [{'source_ip': '192.168.1.100', 'status': 'spoofed'}]
