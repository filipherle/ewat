import urllib2
import sys
import time
from appearance.hue import *
import random

number = str(random.randint(10,10000))
f1 = "output/clickjack-" + number + ".html"

def check_for_vulnerability(url):
    try:
        if "http" not in url:
            url_run = "http://" + url
        data = urllib2.urlopen(url_run)
        headers = data.info()

        if not "X-Frame-Options" in headers:
            html_code = """<html>
    <head>
        <title>Clickjacking test</title>
        <script type="text/javascript" src="clickjack.js"></script>
    </head>
    <body>
        <h1>Clickjacking/framing vulnerability</h1>
        <br/>
        <iframe src="{}" id="iframe" width="600px" height="600px"></iframe>
    </body>
</html>
            """.format(url_run)
            f = open("output/clickjack-" + number + ".html","w")
            f.write(html_code)
            f.close()
            return True
    except:
        return False

def run_clickjacking():
    print (info("Enter the website - eg. www.example.com"))
    url = raw_input(que("Website: "))
    if check_for_vulnerability(url):
        print (good("The website is vulnerable to clickjacking!"))
        print (run("Writing HTML Proof of concept (POC)..."))
        print (info("Created a POC and saved to " + f1))
    elif not check_for_vulnerability(url):
        print (bad("The website is not vulnerable"))
