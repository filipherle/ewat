import time
import os
import sys
from appearance.hue import *
def run_clean():
    print (info("This option will clean up/delete all unnecessary files/folders. This includes the output folder, packages that are no longer needed, .pyc files, systemd journal logs from the last month, Swap Space, PageCache, dentries and inodes."))
    agree = input(que("Are you sure you want to proceed? [Y/n]: "))
    if agree == "yes" or "y" or "Yes" or "Y" or "":
        #print run('Thank you, enjoy EWAT!')
        if os.path.exists("output"):
            print (run("Deleting output/"))
            os.system("sudo rm -rf output/")
        print (run("Cleaning local repository"))
        os.system("sudo apt-get clean")
        print (run("Deleting .pyc files"))
        os.system("cd appearance/ && find . -name '*.pyc' -delete && cd ..")
        os.system("cd modules/ && find . -name '*.pyc' -delete && cd ..")
        print (run("Removing packages no longer needed"))
        os.system("sudo apt-get autoremove -y")
        os.system("sudo apt-get autoclean")
        print (run("Removing systemd journal logs"))
        os.system("sudo journalctl --vacuum-time=30d")
        print (run("Clearing page cache, dentries and inodes"))
        os.system('sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"')
        print (run("Clearing Swap Space"))
        os.system('sudo sh -c "swapoff -a && swapon -a"')
        time.sleep(1)
        print (good("Done!"))
    else:
        time.sleep(1)
