import time
import os
import sys
from appearance.hue import *
import errno
from inspect import currentframe, getframeinfo
def run_error_handling(error_e):
    #print run("Writing to error log.")
    while True:
        if os.path.exists("output"):
            print (run("Writing to output/error.log"))
            frameinfo = getframeinfo(currentframe())
            #print(frameinfo.filename, frameinfo.lineno)
            FILE = open("output/error.log","a+")
            FILE.write(str(error_e) + "\n\n------------------------------------------------------------------\n\n")
            FILE.close()
            break
        else:
            print (run("Creating output folder"))
            os.system("mkdir output")
            continue
            #time.sleep(1)
            #print good("Done!")
