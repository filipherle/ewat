# coding=utf-8
import os
import time
import qrcode
from appearance.hue import *
def run_qrcode():
    url_text = raw_input(que("Website or text: "))
    print ("Enter the name of the output file without the extension")
    name = input(que("Output: "))
    if os.path.isdir("output"):
        os.system("qr " + url_text + " > output/" + name + ".png")
    else:
        os.system("mkdir output")
        os.system("qr " + url_text + " > output/" + name + ".png")
    print (good("QRCode has been generated!" ))
