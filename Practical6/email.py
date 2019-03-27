# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:00:58 2019

@author: HP
"""

import re
#use open() function to open address_information.csv
fhand = open('address_information.csv', 'r')
inp = fhand.read()
print(inp)

#get the comma-separated information using regex re.split()
#comma = re.split(r",", inp)
#print(comma)

#find which address is legal and discard the wrong ones re.match()
x = re.findall (r"[\w\-.]+@[\w\-.]+", inp)
print(x)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#sender_email = input("Type your email:")
#password = input ("Type your password:")
msg = MIMEMultipart()
#msg['From'] = sender_email
msg['Subject'] = "Who just sent me an email?"
body = "Test test test"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.zju.edu.cn', 25)
#Next, log in to the server

#server.login(sender_email, password)


name = re.findall(r"(\S+):", inp)
i = 0
x[i] = x[0]
while i < len(name):
    if x[i] != (r"[.com$]", inp):
        print(i)
        d = name[i]
        address = x[i]
        print(address)       
        note = open('body.txt', 'r')
        e = note.read()
        l = re.sub(r"User",d, e)
        print(l)
        #server.sendmail(sender_email, address, msg.as_string())
       
    else:
        del x[i], name[i]
    i = i + 1  