import urllib
from appearance.hue import *
def run_web():
    try:
        print (info("Enter website - e.g. http://example.com"))
        web = input(que('Website: '))
    except IOError:
        print (bad('Host is in wrong format - e.g. http://example.com' ))
    response = urllib.urlopen(web)
    print ('RESPONSE:', response)
    print ('URL     :', response.geturl())

    headers = response.info()
    print ('DATE    :', headers['date'])
    print ('HEADERS :')
    print ('---------')
    print (headers)

    data = response.read()
    print ('LENGTH  :', len(data))
    print ('---------')
