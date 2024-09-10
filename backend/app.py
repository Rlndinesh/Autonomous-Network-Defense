

# v1

from flask import Flask, jsonify, request
from anomaly_detection import detect_anomalies
from arp_spoofing import monitor_arp, stop_arp_spoofing
from firewall import block_ip, get_open_ports
import threading

app = Flask(__name__)

# Global variables to store network traffic and blocked traffic
network_traffic = []
blocked_traffic = []

@app.route('/')
def index():
    return "Autonomous Network Defense System is Running!"

@app.route('/favicon.ico')
def favicon():
    return "", 204  # Empty response for favicon requests

@app.route('/network/traffic', methods=['GET'])
def get_network_traffic():
    global network_traffic
    return jsonify(network_traffic)

@app.route('/network/blocked', methods=['GET'])
def get_blocked_traffic():
    global blocked_traffic
    return jsonify(blocked_traffic)

@app.route('/network/ports', methods=['GET'])
def get_ports():
    ports = get_open_ports()
    return jsonify(ports)

@app.route('/firewall/block', methods=['POST'])
def block_traffic():
    ip = request.json.get('ip')
    result = block_ip(ip)
    return jsonify({'status': result})

@app.route('/anomaly/detect', methods=['POST'])
def analyze_traffic():
    anomalies = detect_anomalies(network_traffic)
    return jsonify({'anomalies': anomalies})

def arp_spoof_handler(ip):
    global blocked_traffic
    # Capture ARP spoofing and add it to the blocked traffic log
    blocked_message = f"ARP Spoofing Detected: {ip} is spoofed! Blocking {ip}"
    blocked_traffic.append(blocked_message)
    block_ip(ip)  # Block the spoofed IP

if __name__ == "__main__":
    # Run ARP spoof detection in background and capture events
    arp_thread = threading.Thread(target=monitor_arp, args=(arp_spoof_handler,))
    arp_thread.daemon = True
    arp_thread.start()

    app.run(host='0.0.0.0', port=5000)





# from flask import Flask, jsonify, request
# from anomaly_detection import detect_anomalies
# from arp_spoofing import monitor_arp, stop_arp_spoofing
# from firewall import block_ip, get_open_ports
# import threading

# app = Flask(__name__)

# network_traffic = []

# @app.route('/network/traffic', methods=['GET'])
# def get_network_traffic():
#     global network_traffic
#     return jsonify(network_traffic)

# @app.route('/network/ports', methods=['GET'])
# def get_ports():
#     ports = get_open_ports()
#     return jsonify(ports)

# @app.route('/firewall/block', methods=['POST'])
# def block_traffic():
#     ip = request.json.get('ip')
#     result = block_ip(ip)
#     return jsonify({'status': result})

# @app.route('/anomaly/detect', methods=['POST'])
# def analyze_traffic():
#     anomalies = detect_anomalies(network_traffic)
#     return jsonify({'anomalies': anomalies})

# if __name__ == "__main__":
#     # Run ARP spoof detection in background
#     arp_thread = threading.Thread(target=monitor_arp)
#     arp_thread.daemon = True
#     arp_thread.start()

#     app.run(host='0.0.0.0', port=5000)
