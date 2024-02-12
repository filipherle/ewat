#!/usr/bin/python
import os, sys, platform
import time
from appearance.hue import *

def run_ducky_help():
    print (info("Ducky Commands:"))
    print ("""
   ALT [key name] (ex: ALT F4, ALT SPACE)
   CTRL | CONTROL [key name] (ex: CTRL ESC)
   CTRL-ALT [key name] (ex: CTRL-ALT DEL)
   CTRL-SHIFT [key name] (ex: CTRL-SHIFT ESC)
   DEFAULT_DELAY | DEFAULTDELAY [Time in millisecond * 10] (change the delay between each command)
   DELAY [Time in millisecond * 10] (used to overide temporary the default delay)
   GUI | WINDOWS [key name] (ex: GUI r, GUI l)
   REM [anything] (used to comment your code, no obligation)
   ALT-SHIFT (swap language)
   SHIFT [key name] (ex: SHIFT DEL)
   STRING [any character of your layout]
   REPEAT [Number] (Repeat last instruction N times)
   [key name] (anything in the keyboard.properties)
""")
def run_ducky_script():
    scripts = "null"
    try: 
        os.makedirs("output")
    except OSError:
        if not os.path.isdir("output"):
            raise
    print (info("Now we will save 2 files, an encoded one to put onto the ducky, and a text file so you can go back if you messed something up."))
    file_name = raw_input(que("Text file name: "))
    output = raw_input(que("Output file: "))
    print (info("Type your code here (hit ENTER to go to a new line) and when your done type DONE in all caps on a new line. Be careful as you cannot go back."))
    while scripts != 'DONE':
        scripts = raw_input(": ")
        if scripts == "DONE":
            print (run("Generating payload..."))
            FILE = open("output/" + file_name,"a+")
            for line in FILE.readlines():
                cleaned_line = line.replace(scripts,"")
            FILE.close()
            os.system("java -jar extra/duckencoder.jar -i output/" + file_name + " -o " + "output/" + output)
            print (good("Successfully encoded!"))
            time.sleep(1)
        else:
            FILE = open("output/" + file_name,"a+")
            FILE.write(scripts + "\n")
            FILE.close()


def run_ducky_encode():
    print (info("Include .txt and .bin in file names. Use full path."))
    encode = raw_input(que("Text file to be encoded: "))
    print (info("Remember, for the script to execute on the victim computer, it has to be called inject.bin"))
    output = raw_input(que("Output file: "))
    try: 
        os.makedirs("output")
    except OSError:
        if not os.path.isdir("output"):
            raise
    try:
        os.system("java -jar extra/duckencoder.jar -i " + encode + " -o " + "output/" + output)
        print (good("Successfully encoded!"))
        time.sleep(1)
    except:
        print (bad("Error"))
        time.sleep(1)

