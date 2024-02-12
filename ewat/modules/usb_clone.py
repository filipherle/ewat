import pyudev
from time import sleep
import platform
import sys
import os
import subprocess
import shutil
import time
import random
from appearance.hue import *
from appearance.error_handling import *
import errno

def file_clone_device(addr):
    global c_val
    global dest
    print(run("Copying {} files to {}...").format(addr,dest))
    try:
        os.makedirs("output")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    dir_name = "output/" + str(random.getrandbits(10))
    os.mkdir(dir_name)
    try:
        subprocess.call('mount '+addr+' '+dir_name, shell=True)
        time.sleep(1)
    except:
        print(bad("Unable to mount {} -> {}").format(addr,dir_name))
        f = open(dir_name+'/x', 'w+')
        f.close()
        shutil.rmtree(dir_name)
        return 1
    if(os.path.exists(dest)):
        c_dir = os.getcwd()
        os.chdir(dest)
        f = open('x', 'w+')
        f.close()
        os.chdir(c_dir)
        shutil.rmtree(dest)
    else:
        pass
    try:
        c_dir = os.getcwd()
        os.chdir(dir_name)
        time.sleep(1)
        os.chdir(c_dir)
        shutil.copytree(dir_name,dest)
        print(good("Copied files from {} to {}").format(addr,dest))
        try:
            subprocess.call('umount '+addr, shell=True)
        except:
            print(bad("Unable to dismount: {}").format(addr))
            return 2
        return 0
        #shutil.rmtree(dir_name)
    except:
        print(bad("Unable to copy files of {}").format(addr))
        return 1

def run_usb_copy():
    global dest
    #print (info("Please type the full path of where to copy the files"))
    num = random.randint(1,101)
    dest = "output/usb-output-" + str(num) #raw_input(que('Where to copy files: '))
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='block')

    current_partitions = []
    for device in context.list_devices(subsystem='block'):
        if(device.device_node not in current_partitions):
            print(info("Found device {} at Memory Location: {}").format(device.device_node, hex(id(device.device_node))))
            current_partitions.append(device.device_node)

    print(run("Waiting for a partition/USB device..."))
    for device in iter(monitor.poll, None):
        try:
            if device.action == 'add':
                if device.device_type == "partition":
                    print (info("Detected disk/partition: {}".format(device.device_node)))
                    #print(device.get('ID_FS_LABEL', 'unlabeled partition'))
                    data = file_clone_device(device.device_node)
                    if(data == 1):
                        print(bad("The process was unsucessfully initiated on {} ").format(device.device_node))
                        break
                    elif(data == 2):
                        print(info("The process was successfully completed but could not dismount {} ").format(device.device_node))
                        break
                    elif(data == 0):
                        print(good("The process was completed successfully on {} ").format(device.device_node))
                        break
                else:
                    print (bad("Type disk detected but not a partition... moving on"))
            elif device.action == "remove":
                print (info("USB device removed"))
                continue
        except Exception as e:
            print (bad("Something happened! Printing error: "))
            print (e)
            run_error_handling(e)
            return
