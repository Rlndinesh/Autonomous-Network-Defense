import random

# Simulate anomaly detection based on thresholds or machine learning models
def detect_anomalies(traffic_data):
    anomalies = []
    for packet in traffic_data:
        if random.random() > 0.9:  # Example threshold for detection
            anomalies.append(packet)
    return anomalies
