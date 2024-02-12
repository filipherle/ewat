import os, io, platform, sys, socket
from time import sleep
from urllib2 import urlopen
from getmac import get_mac_address as gma

def run_info():
    mac_address = gma()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        localaddr = s.getsockname()[0] # local subnet
    except:
        localaddr="none"

    try:
        ipaddr = urlopen('http://ip.42.pl/raw').read()
    except:
        ipaddr="none"
    try:
        def_gw_device = os.popen("route | grep '^default' | grep -o '[^ ]*$'").read()
    except: 
        def_gw_device = "none"
    print ("+-----------------------------------+")
    print ("| Mac Address: " + str(mac_address))
    print ("+-----------------------------------+")
    print ("| Local Address: " + localaddr)
    print ("+-----------------------------------+")
    print ("| IP Address: " + ipaddr)
    print ("+-----------------------------------+")
    print ("| Platform: " + platform.platform())
    print ("+-----------------------------------+")
    print ("| Name: " + platform.node())
    print ("+-----------------------------------+")
    print ("| Interface: " + def_gw_device + "+-----------------------------------+")
