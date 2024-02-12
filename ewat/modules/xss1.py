import requests
from random import randint
from appearance.hue import *
import os, errno

def run_xss_tester():
    fname = "appearance/payloads.txt"
    with open(fname) as f:
        content = f.readlines()
    payloads = [x.strip() for x in content]
    print (info("Website link needs to end in a parameter, eg. https://www.example.com/uid="))
    url = raw_input(que("Website: "))
    if "https://" or "http://" not in url:
        url = "http://" + url
    vuln = []

    for payload in payloads:
        payload = payload
        xss_url = url + payload
        r = requests.get(xss_url)
        if payload.lower() in r.text.lower():
            print(good("Vulnerable: " + payload))
            if(payload not in vuln):
                vuln.append(payload)
        else:
            continue

    for _ in range(10):
        value = randint(0, 5000)
        value1 = str(value)

    if len(vuln) == 0:
        print (bad("The specified website is not vulnerable to XSS"))
    else:
        print (good("Available Payloads have been recorded in: output/xss-report-" + value1 + ".txt"))
        try:
            os.makedirs("output")
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        with open("output/xss-report" + value1 + ".txt", "w+") as file:
            file.write("Available payloads: " + '\n\n'.join(vuln))
            file.close()
