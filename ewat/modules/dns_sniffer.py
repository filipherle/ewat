#!/usr/bin/env python
import os, sys, socket
import scapy
from scapy.all import *
import subprocess
import dns
from appearance.hue import *
from dns import reversename, resolver

def run_dns_sniff():
    print (info("Please input the IP address of the machine you want to sniff DNS traffic from - eg. 192.168.0.1"))
    host = raw_input(que("IP Address to sniff: "))
    addr = reversename.from_address(host)
    device_name = resolver.query(addr, "PTR")[0]
    with open("/proc/sys/net/ipv4/ip_forward", "w+") as ip_file:
        if ip_file.read() == 1:
            print(good("IP Routing enabled"))
        else:
            ip_file.write("1")
            print(good("IP Routing enabled"))
    print (run("Sniffing DNS traffic from: " + str(device_name)))
    while True:
        try:
            packet = sniff(count=1)
            for pck in packet:
                if(pck.haslayer(IP)):
                    if(pck.haslayer(DNS)):
                        try:
                            hostname = pck.getlayer(DNS).qd.qname
                        except:
                            hostname = 'unknown'
                    if(pck.getlayer(IP).src == host):
                        try:
                            server0 = reversename.from_address(str(pck.getlayer(IP).dst))
                            server1 = resolver.query(server0, "PTR")[0]
                        except:
                            server1 = 'unknown'
                    elif(pck.getlayer(IP).dst == host):
                        try:
                            server0 = reversename.from_address(str(pck.getlayer(IP).src))
                            server1 = resolver.query(server0, "PTR")[0]
                        except:
                            server1 = 'unknown'
                    ip_src = pck.getlayer(IP).src
                    ip_dst = pck.getlayer(IP).dst
                    if(pck.haslayer(DNS)):
                        print(info("{} --> {} - {} | Server: {}").format(ip_src,ip_dst,hostname,server1))
                    else:
                        if(pck.getlayer(IP).src == host):
                            try:
                                server0 = reversename.from_address(str(pck.getlayer(IP).dst))
                                server1 = resolver.query(server0, "PTR")[0]
                            except:
                                server1 = 'unknown'
                        elif(pck.getlayer(IP).dst == host):
                            try:
                                server0 = reversename.from_address(str(pck.getlayer(IP).src))
                                server1 = resolver.query(server0, "PTR")[0]
                            except:
                                server1 = 'unknown'
                        print(info("{} --> {} | Server: {}").format(ip_src,ip_dst,server1))
        except KeyboardInterrupt:
            print (bad("Exiting..."))
            time.sleep(1)
            break
        except:
            pass
