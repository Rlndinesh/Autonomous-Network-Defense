import os

def block_ip(ip):
    try:
        os.system(f"netsh advfirewall firewall add rule name='Block {ip}' dir=in action=block remoteip={ip}")
        return "Success"
    except Exception as e:
        return str(e)

def get_open_ports():
    # Use Nmap or Python socket library to get open ports
    ports = ['80', '443', '22']  # Simulated data for example
    return ports
