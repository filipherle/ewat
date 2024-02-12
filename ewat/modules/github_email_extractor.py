#!/usr/bin/env python
import sys
import subprocess
import time
import os
import requests
import errno
from appearance.hue import *

def run_get_github():
    error = 1
    username = raw_input(que("Github Username: "))
    print (run("Extracting email..."))
    r = requests.get('https://api.github.com/users/'+str(username)+'/events/public')
    try:
        os.makedirs("output")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    f = open('output/g_email_parse.data', 'w+')
    f.truncate()
    f.write(str(r.content))
    f.close()
    f = open('output/g_email_parse.data', 'r')
    for line in f:
        if('"email":' in line.strip()):
            string = str(str(line.strip().split('"email":')[1]).split('","n')[0])[1:]
            print (good("Email: " + str(string)))
            #f.close()
            #os.remove('output/g_email_parse.data')
            error = 0
        elif('"location":' in line.strip()):
            string = str(str(line.strip().split('"location":')[1]).split('","n')[0])[1:]
            print (good("Location: " + str(string)))
            error = 0
        f.close()
        os.remove('output/g_email_parse.data')
        break
    if(error != 0):
        print (bad('Error. Could not gather email'))
