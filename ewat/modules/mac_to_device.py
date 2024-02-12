import requests
from appearance.hue import *
def run_device_mac():
    device_mac = raw_input(que("MAC Address: "))
    r = requests.get('http://macvendors.co/api/'+str(device_mac))
    device_type = r.content.split('","mac_')[0].replace('{"result":{"company":"', '')
    if device_type == """{"result":{"error":"no result"}}""":
        print (bad("Sorry, could not retrieve device type!"))
    else:
        print (info("{} has a MAC Address of {}").format(device_type, device_mac))
