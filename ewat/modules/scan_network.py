import sys
import os
import time
from appearance.hue import *
from appearance.error_handling import *
from scapy.all import Ether, ARP, srp
from random import randint
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
conf.verb = 0

def run_network_scan():
    print (info("Enter the scanning range - eg. 192.168.0.0/24"))
    range1 = input(que("Scanning range: "))
    print (info("Enter the network interface to use - eg. wlan0"))
    interface = input(que("Network interface: "))
    ip, ntBits = range1.split('/')
    st_bit = ip.split('.')[3:4][0]
    ip_addresses = []
    for n in range(1, int(ntBits)+1):
        e_ip = ".".join(ip.split('.')[:-1]) + '.' + str(n)
        ip_addresses.append(e_ip)

    for ip in ip_addresses:
        packet1 = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
        ans, unans = srp(packet1, iface=interface, timeout=0.5, verbose=False)
        for snt, recv in ans:
            if recv:
                print (good("%s | %s" % (recv[ARP].psrc, recv[Ether].src)))
    time.sleep(1)
    os.system("sudo /etc/init.d/network-manager restart")

