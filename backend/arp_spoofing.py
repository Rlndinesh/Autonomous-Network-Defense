
import scapy.all as scapy

def monitor_arp():
    def detect_spoof(packet):
        if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
            # Check for IP and MAC inconsistencies
            real_mac = scapy.getmacbyip(packet[scapy.ARP].psrc)
            if real_mac != packet[scapy.ARP].hwsrc:
                print(f"ARP Spoofing Detected: {packet[scapy.ARP].psrc} is spoofed!")
                stop_arp_spoofing(packet[scapy.ARP].psrc)

    scapy.sniff(store=False, prn=detect_spoof)

def stop_arp_spoofing(ip_address):
    # Block IP from firewall or drop ARP responses
    print(f"Blocking {ip_address} due to ARP spoofing")
