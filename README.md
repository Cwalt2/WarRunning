# 🔧 War Running

> **DISCLAIMER:**
> This software is provided for educational and research purposes only.
> Unauthorized access, surveillance, or tampering with networks or systems that you do not own or have permission to test
> may be a violation of local, state, or federal law.
> The author(s) are not responsible for any misuse of this tool.

## Description

This program is a lightweight and expandable passive network scanner. This can be headless with the correct setup and is compatible with most linux distributions (NOT compatible with Windows machines). All scripts can be run without internet connectivity besides a scanning WiFi card. Logs are saved with network information containing the BSSID, SSID, Signal Strength, Channel, Channel Frequency, Rates, and Encryption.

## 📁 Features

- Scans continously for Wi-Fi networks
- Availability on ARM/mobile devices
- Store individual network logs for later analysis
- Easy headless setup

## 💻 Technologies Used

- Python
- Scapy
- Old Wi-Fi card
- Raspberry Pi 4/Zero W 2
- Aircrack-ng suite
- Pi OS lite (64-bit)
- INIU Power Bank (5V/3A - 10000mAh/37Wh)

## Hard Requirements

- Linux based OS
- aircrack-ng
- scapy > 2.5.0
- python
- Wi-Fi card with monitoring/promiscuous capability

## 🚀 Getting Started

Clone the repo:

```bash

git clone https://github.com/Cwalt2/WarRunning.git
```

Then cd into the file and install requirements/dependencies:

```bash

# aircrack-ng is required
sudo apt update
sudo apt install aircrack-ng -y
# install depends on OS

# Virtual environment heavily preferred
cd WarRunning

pip install -r requirements.txt
```

prepare your WiFi card

```bash

# find your Wi-Fi card using iwconfig
sudo iwconfig

# start monitoring mode replacing wlan0 with your card name
sudo airmon-ng start wlan0
```

make file executable then start using elevated permissions

```bash
chmod +x main.py

# you may need to modify the line at the top of this file
sudo ./main.py
# ex. #!/home/user/env-name/network-sniffer/bin/python
```

After running the python script you should see the program scanning for networks in your immediate area

``` bash
[+] New Network Found
SSID            : <Hidden>
BSSID           : ff:ff:ff:ff:ff:ff
Signal Strength : -52 dBm
Channel         : 10
Freq            : 2457 MHz
Rates           : 1.0 2.0 5.5 11.0 18.0 24.0 36.0 54.0 6.0 9.0 12.0 48.0 Mbps
Encryption      : WPA2/PSK

[+] New Network Found
SSID            : <Hidden>
BSSID           : ff:ff:ff:ff:ff:ff
Signal Strength : -59 dBm
Channel         : 10
Freq            : 2457 MHz
Rates           : 1.0 2.0 5.5 11.0 18.0 24.0 36.0 54.0 6.0 9.0 12.0 48.0 Mbps
Encryption      : WPA2/PSK

[+] New Network Found
SSID            : <Hidden>
BSSID           : ff:ff:ff:ff:ff:ff
Signal Strength : -58 dBm
Channel         : 7
Freq            : 2457 MHz
Rates           : 1.0 2.0 5.5 11.0 9.0 18.0 36.0 54.0 6.0 12.0 24.0 48.0 Mbps
Encryption      : WPA2/PSK

[+] New Network Found
SSID            : <Hidden>
BSSID           : ff:ff:ff:ff:ff:ff
Signal Strength : -67 dBm
Channel         : 10
Freq            : 2457 MHz
Rates           : 1.0 2.0 5.5 11.0 6.0 9.0 12.0 18.0 24.0 36.0 48.0 54.0 Mbps
Encryption      : WPA2/PSK

[+] New Network Found
SSID            : <Hidden>
BSSID           : ff:ff:ff:ff:ff:ff
Signal Strength : -71 dBm
Channel         : 10
Freq            : 2457 MHz
Rates           : 1.0 2.0 5.5 11.0 6.0 9.0 12.0 18.0 24.0 36.0 48.0 54.0 Mbps
Encryption      : OPN
```

## Start Scripts

`start.sh` autostarts the WarRunning script in the background and continues running despite losing connection
The script saves logs to a output file in the logs folder.
> NOTE: this will overwrite after every execution

In order to execute this script you will need to make it executable first

```bash

chmod +x start.sh
sudo ./start.sh
```

## TODO

- [ ] Example video
- [ ] Auto cracking script
- [ ] Attack examples
- [ ] Rust implementation
- [ ] Threading?
- [x] Auto start/stop scripts
- [ ] Test frequency detection in depth

## Extras

I also added a script that inspired/helped me create the WarRunning script, made by [SleepTheGod](https://github.com/SleepTheGod/Wifi-Scanner)

```bash

chmod +x static-script.py
./static-script.py
```

If all goes well you will be asked to input your interface, then it scans your immediate area and outputs the networks.
