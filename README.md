# 🛰️ Layer 2 VPN Virtual Switch

A Python-based Layer 2 Virtual Private Network (VPN) implementation using TAP devices on Linux. This tool replicates Ethernet frame exchange in a virtualized environment, mimicking the behavior of a traditional Layer 2 switch.

## 🔧 Features

- Emulates Layer 2 switching behavior using TAP interfaces  
- Supports multiple TAP devices for inter-device communication  
- Uses raw Ethernet frame processing via Python sockets  
- Simple configuration via `config.yaml`  
- Modular code design for easy extension

## 📁 Project Structure

```
l2vpn_virtual_switch/
│
├── l2_switch.py         # Main switch logic handling TAP interfaces
├── tap_utils.py         # TAP device setup and I/O operations
├── config.yaml          # YAML configuration for interface settings
├── run.sh               # Shell script to run the project (Linux only)
└── README.md            # Project documentation
```

## 🛠️ Setup

> ⚠️ **Note**: This project is designed for Linux. Use WSL2 (Ubuntu) if running on Windows.

1. **Install Python dependencies**  
```bash
pip install pyyaml
```

2. **Enable TAP support in Linux (if needed)**  
Ensure `/dev/net/tun` is available. You might need to load the kernel module:
```bash
sudo modprobe tun
```

3. **Run the project (WSL/Linux)**  
```bash
sudo bash run.sh
```

## ⚙️ Configuration (`config.yaml`)

```yaml
tap_interfaces:
  - tap1
  - tap2
```

Define your virtual TAP interfaces for bridging.

## ✅ Example Output

```
[*] Creating TAP interface: tap1
[*] Creating TAP interface: tap2
[+] Starting Layer 2 VPN Switch
[+] Listening on tap1, tap2 for Ethernet frames...
```

## 📌 Use Cases

- Educational tool for understanding Layer 2 behavior  
- Testing Ethernet-level frame forwarding in virtual labs  
- Building foundational concepts for SDN, VPNs, and tunneling protocols

## 🧠 Interview Tip

Highlight this project as:

- A demonstration of low-level network programming using Python and Linux networking
- A foundational understanding of TUN/TAP, Ethernet switching, and virtual interfaces
- A bridge between software-defined networking (SDN) concepts and hands-on network emulation

