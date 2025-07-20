# l2_switch.py
# Implements Layer 2 switching logic with MAC learning and forwarding

import tap_utils
import yaml
import select
import time

MAC_TABLE = {}  # MAC -> Interface

def learn_mac(mac, iface):
    MAC_TABLE[mac] = (iface, time.time())

def lookup_mac(mac):
    entry = MAC_TABLE.get(mac)
    if entry:
        return entry[0]
    return None

def cleanup_mac_table(timeout=300):
    now = time.time()
    for mac in list(MAC_TABLE.keys()):
        if now - MAC_TABLE[mac][1] > timeout:
            del MAC_TABLE[mac]

def main():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    tap_interfaces = {}
    fds = []

    for entry in config['interfaces']:
        name = entry['name']
        fd = tap_utils.create_tap(name)
        tap_interfaces[fd] = name
        fds.append(fd)
        print(f"[+] TAP interface {name} created.")

    print("[*] Virtual switch started.")

    while True:
        cleanup_mac_table()
        rlist, _, _ = select.select(fds, [], [], 1)

        for fd in rlist:
            frame = tap_utils.read_frame(fd)
            if frame:
                dst_mac = frame[0:6]
                src_mac = frame[6:12]
                learn_mac(src_mac, fd)

                out_fd = lookup_mac(dst_mac)
                if out_fd and out_fd != fd:
                    tap_utils.write_frame(out_fd, frame)
                else:
                    for other_fd in fds:
                        if other_fd != fd:
                            tap_utils.write_frame(other_fd, frame)

if __name__ == "__main__":
    main()
