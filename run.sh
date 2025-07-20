#!/bin/bash
# Script to run the Layer 2 VPN Switch

echo "[*] Setting up TAP interfaces..."
sudo ip tuntap add dev tap0 mode tap
sudo ip tuntap add dev tap1 mode tap
sudo ip tuntap add dev tap2 mode tap

sudo ip link set tap0 up
sudo ip link set tap1 up
sudo ip link set tap2 up

echo "[*] Running virtual switch..."
sudo python3 l2_switch.py
