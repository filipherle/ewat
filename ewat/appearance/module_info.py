from hue import *
import sys
import os
def run_module_info(title, author, desc):
    print (blue("Title: ") + title)
    print (blue("Author: ") + author)
    print (blue("Description: ") + desc)
def show_modules():
    print (info("Showing all modules"))
    filepath = 'appearance/modules.txt'
    f = open(filepath, "r")
    print(f.read())
def module_info(module_name):
    if module_name == "xss_test":
        run_module_info("Cross-site scripting vulnerability assessment", "Filip aka toxic", "Tests a website for XSS vulnerabilites")
    elif module_name == "device_mac":
        run_module_info("MAC Address Resolver", "Filip aka toxic", "Resolves a MAC Address")
    elif module_name == "admin":
        run_module_info("Admin Panel Finder", "Filip aka toxic", "Attempts to find the Adminstrator panel of a website.")
    elif module_name == "email_spoof":
        run_module_info("Email Spoofer", "Filip aka toxic", "Spoofs an email")
    elif module_name == "image":
        run_module_info("Image Modules", "Filip aka toxic", "Extracts metadata and valuable information from an image/strips metadata")
    elif module_name == "cred_harvest":
        run_module_info("Credential Harvester", "Filip aka toxic", "Copies a website, runs it on the network, and harvests credentials")
    elif module_name == "list_ssid":
        run_module_info("SSID Lister", "Filip aka toxic", "Scans and lists networks in range")
    elif module_name == "clickjacking":
        run_module_info("Clickjacking Tester", "Filip aka toxic", "Tests a website for the clickjacking vulnerability")
    #elif module_name == "zipfile_crack":
        #run_module_info("Zipfile Cracker", "Filip aka toxic", "Runs a dictionary attack against a zipfile")
    elif module_name == "scan_devices":
        run_module_info("Network Scanner", "Filip aka toxic", "Scans the network for active hosts")
    elif module_name == "github":
        run_module_info("Github Email Extractor", "Filip aka toxic", "Extracts a user's email from Github")
    elif module_name == "ducky_script":
        run_module_info("USB Rubber Ducky Module", "Filip aka toxic", "Encode/Write a rubber ducky script")
    #elif module_name == "sql_test":
        #run_module_info("SQL Vulnerability tester", "Filip aka toxic", "Tests a website for SQL vulerabilities")
    elif module_name == "rom0_exploit":
        run_module_info("Rom0 exploit checker", "Filip aka toxic", "Tests a website for the simple rom0 exploit and downloads the file if vulnerable")
    elif module_name == "comp_info":
        run_module_info("Computer information", "Filip aka toxic", "Shows simple computer/network information")
    elif module_name == "http_sniffer":
        run_module_info("HTTP Sniffer", "Filip aka toxic", "Sniffs any unencrypted traffic on the desired target - http requests, unsecure logins, etc.")
    elif module_name == "arp_spoof":
        run_module_info("ARP Spoofer", "Filip aka toxic", "Simply spoofs ARP requests")
    elif module_name == "usb":
        run_module_info("USB Module", "Filip aka toxic", "Do all sorts of cool stuff with USB's. Helpful on a penetration test or simply working at home. Clone them, infect them, and more!")
    elif module_name == "dns_sniff":
        run_module_info("DNS Sniffer", "Filip aka toxic", "Sniffs DNS traffic from a device on the network. Can be used with the ARP spoofer.")
