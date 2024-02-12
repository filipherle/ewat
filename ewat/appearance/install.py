from subprocess import call
import os.path
import time
from appearance.hue import *
from appearance.agree import *
def install_script():
        def run_install_script():
                call("sudo apt-get update", shell=True)
                call("sudo apt-get install python-pip python-setuptools python-wheel", shell=True)
                call("sudo apt-get install python-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python-pip git default-jdk", shell=True)
                import pip
                try:
                        import setuptools 
                except:
                        pip.main(['install', 'setuptools'])
                try:
                        import pyudev
                except:
                        pip.main(['install','pyudev'])
                try:
                        import scapy
                except:
                        pip.main(['install','scapy'])
                try:
                        from PIL import Image
                except:
                        pip.main(['install', 'Pillow'])
                try:
                        import dns
                except:
                        pip.main(['install','pydns'])
                try:
                        import scapy_http
                        from scapy_http import http
                except:
                        pip.main(['install','scapy-http'])
                try:
                        import proxyscrape
                except:
                        pip.main(['install','proxyscrape'])
                try:
                        from GPSPhoto import gpsphoto
                except:
                        pip.main(['install','pathlib'])
                        pip.main(['install','gpsphoto'])
                try:
                        import piexif
                        import exifread
                except:
                        pip.main(['install','piexif'])
                        pip.main(['install', 'exifread'])
                try:
                        import socks
                except:
                        pip.main(['install','pysocks'])
                        pip.main(['install','socks'])
                try:
                        import pychromecast
                except:
                        pip.main(['install', 'pychromecast'])
                try:
                        import requests
                except:
                        pip.main(['install', 'requests'])
                try:
                        import flask
                except:
                        pip.main(['install', 'flask'])
                try:
                        import re
                except:
                        pip.main(['install', 're'])
                try:
                        import requests
                except:
                        pip.main(['install', 'requests'])
                try:
                        import qrcode
                except:
                        pip.main(['install', 'qrcode[pil]'])
                try:
                        import getmac
                except:
                        pip.main(['install', 'getmac'])
                print (good("Successfully installed!"))
                f = open("appearance/installed.txt","w+")
                f.close()
                run_agree()
                call("sudo mkdir /opt/ewat && sudo cp EWAT.py /opt/ewat && sudo cp -R appearance/ /opt/ewat && sudo cp -R modules/ /opt/ewat && sudo cp ewat /usr/local/bin/ && sudo cp ewat /usr/local/bin/ && sudo chmod +x /usr/local/bin/ewat && sudo cp ewat_uninstall /usr/local/bin/ && sudo chmod +x /usr/local/bin/ewat_uninstall", shell=True)
        if os.path.exists("appearance/installed.txt"):
                print (good("EWAT installed. No need to install again"))
                time.sleep(0.2)
                #print run("Loading EWAT...")
                run_agree()
        else:
                run_install_script()
