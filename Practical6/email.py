# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:00:58 2019

@author: HP
"""

import re
#use open() function to open address_information.csv
address_book = open('address_information.csv', 'r')
address_open = address_book.read()

#find which address is legal (with .com)
valid_address = re.findall (r"[\w\-.]+@[\w\-.]+.com", address_open)
print(valid_address)
#extract the receiver from the spreadsheet
receiver = re.findall(r"(\S+):", address_open)
#Delete David. I have been trying to figure out how to delete David automatically.
#I tried to make a dictionary like this: {'Anna':'ibifiletest.163.com', 'David':'python@zju'}
#I tried to delete David using this code: 
#for k in dict.keys():
#if k.endswith('.com') is False:
#del dict(k)
#However, the code would not work. Therefore, for now, I manually delete David.
del receiver[1]
print(receiver)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Login to the ZJU email server
sender_email = input("Your ZJU email:")
password = input("Password:")
server = smtplib.SMTP('smtp.zju.edu.cn', 25)
server.login(sender_email, password)

i = 0
for i in range (len(receiver)):
    count_receiver = receiver[i]
    count_address = valid_address[i]
    print("The email has been sent to " +valid_address[i])
    text = open('body.txt', 'r')
    text_open = text.read()
    #To address the email recipient by name
    change_username = re.sub(r"User",count_receiver, text_open)
    message = MIMEMultipart()
    message['From'] = "Adele"
    message['Subject'] = "Dear " +count_receiver + ", Your Analysis Job Has Been Completed"
    message.attach(MIMEText(change_username, 'plain'))
    server.sendmail(sender_email, count_address, message.as_string()) 
    i = i + 1