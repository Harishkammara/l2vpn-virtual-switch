# tap_utils.py
# TAP device handling utilities

import fcntl
import os
import struct

TUNSETIFF = 0x400454ca
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000

def create_tap(ifname='tap0'):
    tap = os.open('/dev/net/tun', os.O_RDWR)
    ifr = struct.pack('16sH', ifname.encode('utf-8'), IFF_TAP | IFF_NO_PI)
    fcntl.ioctl(tap, TUNSETIFF, ifr)
    return tap

def read_frame(fd):
    try:
        return os.read(fd, 1600)
    except OSError:
        return None

def write_frame(fd, frame):
    try:
        os.write(fd, frame)
    except OSError:
        pass
