import time
import os
import sys
from appearance.hue import *
def run_agree():
    print (run("Checking agreement..."))
    if os.path.exists("appearance/agree.txt"):
        print (good("Agreement is signed."))
        print (run("Loading EWAT..."))
    else:
        print (bold("""
Note that EWAT is provided as is, and is a royalty free open-source application.

Feel free to modify, use, change, market, do whatever you want with it as long as you give the appropriate credit where credit is due (which means giving the authors the credit they deserve for writing it).

If you are planning on using this tool for malicious purposes that are not authorized by the company you are performing assessments for, you are violating the terms of service and license of this tool.
By hitting yes (only one time), you agree to the terms of service and that you will only use this tool for lawful purposes only.
"""))
        agree = input(que("Do you agree to these terms and conditions?: "))
        if agree == "yes" or "y" or "Yes" or "Y":
            print (good('Thank you, enjoy EWAT!'))
            time.sleep(3)
            FILE = open("appearance/agree.txt","w")
            FILE.write('yes')
            FILE.close()
        else:
            print (bad('You have to agree!'))
            time.sleep(1)
            sys.exit()
