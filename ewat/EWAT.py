#!/usr/bin/env python
#Coding: utf-8
#Developed by: Filip aka 'Toxic'
#Hello fellow developers. Please credit me if you use any of my source code.

#Install script
from appearance.install import *
# Run installation script and agreement
install_script()

# Normal imports
import sys
import os
import time
import readline
import platform as platf
import time
import subprocess
from subprocess import call
import socket
import urllib2


# File imports
from appearance.hue import *
from appearance.logo import *
from appearance.module_info import *
from appearance.agree import *
from appearance.credits import *
from appearance.clean import *
from appearance.joke import *
from appearance.error_handling import *

# Check Necessities
if str(platf.system()) != "Linux":
        print (bad("You are not using a Linux Based OS! Linux is a must-have for this script! Mac OSX and Windows are not yet supported!" ))
        sys.exit()
if not os.geteuid() == 0:
        print (bad("Must be run as root!"))
        sys.exit()

# Check for internet
try:
    urllib2.urlopen('http://8.8.8.8', timeout=2)
    print (good("Internet connection is working"))
except urllib2.URLError as err:
    print (bad("No internet detected! Not all functions will work."))
    time.sleep(4.20) #lol why not haha blaze up baby
    #sys.exit()



# Special file imports / Modules
from modules.PhishingPage import *
from modules.mac_to_device import *
from modules.smtp_s import *
from modules.ssid_list import *
#from modules.zipfile1 import *
from modules.scan_network import *
from modules.xss1 import *
from modules.website_source import *
from modules.qrcode import *
from modules.dns_sniffer import *
from modules.admin import *
from modules.info import *
from modules.web import *
from appearance.version_checker import *
from modules.github_email_extractor import *
from modules.ducky_script import *
from appearance.completion import *
from modules.rom0_exploit import *
from modules.clickjacking import *
from modules.arp import *
from modules.image_metadata import *
from modules.http_sniffer import *
from modules.usb_clone import *
from modules.usb_malware import *
from modules.proxy_finder import *
from modules.mask_ip import *
from modules.strip_metadata import *

# Other stuff
call("clear", shell=True)
help_menu = """
modules       - show all the available modules
[module] info - show info about the module
clean         - Deletes output folder and any unnecessary files/packages/logs (CAREFUL)
joke          - print a joke
banner        - print a new banner
clear         - clear the screen
credits       - show credits
exit          - exit the tool
"""
logo_print()
version_check()
keywords = ["cred_harvest", "qrcode", "exit", "modules", "rom0_exploit", "joke", "help", "options", "comp_info", "web", "clean", "ducky_script", "banner", "admin", "clear", "credits", "github", "list_ssid", "email_spoof", "website_source", "device_mac", "xss_test", "network_scan", "info", "clickjacking", "image", "arp_spoof", "http_sniffer", "usb", "scan_devices", "clone", "type", "dns_sniff", "malware", "mask_ip", "metadata", "strip_metadata", "proxy_scraper"]
completer = Completer(keywords)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

# Main part
while True:
        try:
                command = input(green("root" + red("@") + green("ewat") + white("> ")))
                if(command == 'help' or command == '?' or command == 'options'):
                        print(help_menu)
                elif(command == 'modules'):
                        show_modules()
                elif(command == ''):
                        continue
                elif(command == 'joke'):
                        run_joke()
                elif(command == 'qrcode'):
                        run_qrcode()
                elif(command == 'clickjacking'):
                        run_clickjacking()
                elif(command == 'comp_info'):
                        run_info()
                elif(command == 'arp_spoof'):
                        run_arp_spoof()
                elif(command == 'scan_devices'):
                        run_network_scan()
                elif(command == 'http_sniffer'):
                        run_http_sniffer()
                #elif(command == 'chromecast'):
                        #run_chromecast()
                elif(command == 'web'):
                        run_web()
                elif "image " in command:
                        try:
                            image_command = command.split(" ")[1]
                            if image_command == "metadata":
                                run_metadata()
                            elif image_command == "strip_metadata":
                                run_strip_metadata()
                            elif image_command == "info":
                                module_info("image")
                            elif image_command.strip() == "":
                                print (info("Enter an image module!"))
                            #elif image_command == "type":
                                #run_ducky_script()
                            else:
                                print (bad("Not an image module option!"))
                        except Exception as e:
                            print (bad("Error!"))
                            print (e)
                elif(command == "image"):
                        print (info("Enter an image module"))
                elif(command == 'rom0_exploit'):
                        run_rom0()
                elif(command == 'clean'):
                        run_clean()
                elif "ducky_script " in command:
                        try:
                            ducky_command = command.split(" ")[1]
                            if ducky_command == "help":
                                run_ducky_help()
                            elif ducky_command == "encode":
                                run_ducky_encode()
                            elif ducky_command == "info":
                                module_info("ducky_script")
                            elif ducky_command == "type":
                                run_ducky_script()
                            else:
                                print (bad("Not a ducky script option!"))
                        except:
                            print (bad("Error!"))
                elif(command == 'ducky_script'):
                        print (info("Enter a ducky script option!"))
                elif(command == 'banner'):
                        call("clear", shell=True)
                        logo_print()
                        version_check()
                elif(command == 'admin'):
                        run_admin()
                elif(command == 'dns_sniff'):
                        run_dns_sniff()
                elif(command == 'proxy_scraper'):
                        run_proxy_scraper()
                elif(command == 'clear'):
                        call("clear", shell=True)
                elif(command == 'credits'):
                        run_credits()
                elif(command == 'github'):
                        run_get_github()
                elif(command == 'mask_ip'):
                        run_mask_ip()
                elif(command == 'exit'):
                        print (bad("Exiting..."))
                        sys.exit(2)
                elif(command == 'list_ssid'):
                        try:
                                run_ssid_listt()
                        except Exception as e:
                                print (bad("Something happened! Printing error: "))
                                print (e)
                                run_error_handling(e)
                elif(command == 'cred_harvest'):
                        try:
                                run_credharvest()
                        except Exception as e:
                                print (bad("Something happened! Printing error: "))
                                print (e)
                                run_error_handling(e)
                elif(command == 'ls'):
                        call("ls", shell=True)
                elif(command == 'email_spoof'):
                        try:
                                run_spoof_email()
                        except Exception as e:
                                print (bad("Something happened! Printing error: "))
                                print (e)
                                run_error_handling(e)
                elif "usb " in command:
                        try:
                            usb_command = command.split(" ")[1]
                            if usb_command == "clone":
                                run_usb_copy()
                            elif usb_command == "malware":
                                run_usb_malware()
                            elif usb_command == "info":
                                module_info("usb")
                            #elif usb_command == "type":
                                #run_ducky_script()
                            else:
                                print (bad("Not a USB script option!"))
                        except Exception as e:
                            print (bad("Something happened! Printing error: "))
                            print (e)
                            run_error_handling(e)
                elif(command == "usb"):
                        print (info("Enter a USB module option!"))
                #elif(command == 'zipfile_cracker'):
                        #try:
                                #run_zipfile()
                        #except Exception as e:
                                #print bad("Something happened! Printing error: ")
                                #print e
                                #run_error_handling(e)
                elif(command == 'xss_test'):
                        try:
                                run_xss_tester()
                        except Exception as e:
                                print (bad("Something happened! Printing error: "))
                                print (e)
                                run_error_handling(e)
                elif(command == 'website_source'):
                        try:
                                run_websitesource()
                        except Exception as e:
                                print (bad("Something happened! Printing error: "))
                                print (e)
                                run_error_handling(e)
                elif(command == 'device_mac'):
                        try:
                                run_device_mac()
                        except Exception as e:
                                print (bad("Something happened! Printing error: "))
                                print (e)
                                run_error_handling(e)
                elif(command == 'network_scan'):
                        try:
                                run_network_scan()
                        except Exception as e:
                                print (bad("Something happened! Printing error: "))
                                print (e)
                                run_error_handling(e)
                elif " info" in command:
                        module_command = command.split(" ")[0]
                        module_info(module_command)
                else:
                        print (bad(command + " is not an option"))
        except KeyboardInterrupt:
                print ("\n")
                print (bad("Exiting..."))
                sys.exit(1)
        except Exception as e:
                print ("\n")
                print (bad("Something happened! Printing error: "))
                print (e)
                run_error_handling(e)
