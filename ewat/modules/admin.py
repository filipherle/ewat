from urllib2 import Request, urlopen, URLError, HTTPError
import time
from appearance.hue import *
def run_admin():
    f = open("appearance/admin.txt","r")
    print (info("Enter the website to scan for admin panels - eg. www.example.com"))
    link = input(que('Site: '))
    print (run("Scanning..."))
    print (info("Available links: \n"))
    while True:
        sub_link = f.readline()
        if not sub_link:
            break
        req_link = "http://"+link+"/"+sub_link
        req = Request(req_link)
        try:
            response = urlopen(req)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print (good(req_link))
