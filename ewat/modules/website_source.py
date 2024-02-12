import urllib2
from random import randint
import os, errno

from appearance.hue import *
def run_websitesource():
    print (info("Please input the full website. ie: https://www.example.com"))
    url = input(que("Website: "))
    response = urllib2.urlopen(url)
    page_source = response.read()

    for _ in range(10):
        value = randint(0, 5000)
        value1 = str(value)
    try:
        os.makedirs("output")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    with open("output/website-source-" + value1 + ".html", "w+") as file:
        file.write(page_source)
        file.close()
    print (good("Finished cloning" + url + " into: output/website-source-" + value1 + ".html"))
    print (good("Check the /output directory for HTML source file"))
