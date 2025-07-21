#!/home/user/env-name/bin/python

from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11, Dot11Elt
import os
from datetime import datetime

# Output directory and log file
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_path = os.path.join(log_dir, f"wifi_scan_{timestamp}.log")

# Track discovered networks by BSSID
networks = {}

# Grabs frequency (2.4 GHz/5 GHz) from a network
def channel_to_frequency(channel):
    channel = int(channel)
    if 1 <= channel <= 14:
        return 2407 + (channel * 5)
    elif 36 <= channel <= 165:
        return 5000 + (channel * 5)
    elif 1 <= channel <= 233:  # 6 GHz band (optional)
        return 5950 + (channel * 5)
    else:
        return None

def packet_handler(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode(errors="ignore")
        bssid = packet[Dot11].addr2
        stats = packet[Dot11Beacon].network_stats()
        channel = ord(packet[Dot11Elt:3].info)
        freq = channel_to_frequency(channel)
        signal = packet.dBm_AntSignal
        rates = stats.get("rates")
        crypto = ', '.join(stats.get("crypto", []))

        if bssid not in networks:
            networks[bssid] = {
                "SSID": ssid,
                "Signal": signal,
                "Channel": channel,
                "Rates": rates,
                "Crypto": crypto
            }

            output = (
                f"\n[+] New Network Found\n"
                f"SSID            : {ssid or '<Hidden>'}\n"
                f"BSSID           : {bssid}\n"
                f"Signal Strength : {signal} dBm\n"
                f"Channel         : {channel}\n"
                f"Freq:           : {freq} MHz\n"
                f"Rates           : {' '.join(map(str, rates))} Mbps\n"
                f"Encryption      : {crypto}\n"
            )

            # Log to file
            with open(log_file_path, "a") as f:
                f.write(output)

            # Optional: also print to screen
            print(output)

if __name__ == "__main__":
    # Change this to your wireless interface
    iface = "wlan0"

    print(f"[*] Logging detected Wi-Fi networks to: {log_file_path}")
    print("[*] Scanning... Press Ctrl+C to stop.\n")

    # Sniff continuously and log new networks
    sniff(prn=packet_handler, iface=iface, store=False)
