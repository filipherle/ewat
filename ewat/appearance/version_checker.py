import requests
from appearance.hue import *
import time
def version_check():
    r = requests.get('https://raw.githubusercontent.com/toxic-ig/ewat/master/appearance/version.txt')
    f = open("appearance/version.txt", "r")
    version = f.read()
    print ("      Version -> " + under(version))
    if version not in r.text:
        print (bad('You need to update! The newest version is: ' + r.text))
        print (info("Uninstall EWAT and reinstall the newest version from github."))
        print (info("https://www.github.com/toxic-ig/ewat"))
        time.sleep(3)
