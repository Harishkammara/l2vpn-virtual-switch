# Layer 2 VPN / Virtual Switch (Python + TAP)

This project implements a Layer 2 Virtual Switch using TAP devices and raw Ethernet frames, written in Python.

## 📌 Features
- Ethernet frame capture and forwarding between TAP interfaces
- MAC address learning and aging
- Simulates broadcast behavior for unknown MACs

## 🛠️ Requirements
- Linux system with `/dev/net/tun`
- Python 3.x
- Root privileges

## 📂 Files
- `l2_switch.py`: Switching logic and MAC table
- `tap_utils.py`: TAP interface creation and frame I/O
- `config.yaml`: List of TAP interfaces
- `run.sh`: Bash script to configure interfaces and start the switch

## 🚀 Usage

```bash
chmod +x run.sh
sudo ./run.sh
