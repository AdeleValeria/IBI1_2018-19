# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:00:58 2019

@author: HP
"""

import re
import copy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#to open address_information.csv
address_book = open('address_information.csv', 'r')
address_open = address_book.read()

#find all email addresses in the excel file.
valid_address = re.findall (r"[\w\-.]+@[\w\-.]+", address_open)
#extract all email recipients in the excel file.
receiver = re.findall(r"(\S+):", address_open)
#Make a dictionary to join each email address with its correct user as key:value pair.
dict1 = {key:value for key, value in zip(valid_address, receiver)}
#Use deepcopy to copy the original dictionary to a new dictionary.
#Important to avoid error when deleting an item.
dict2 = copy.deepcopy(dict1)
#Next, remove any invalid email address from the dictionary.
for k in dict1.keys():
    #If an item in the dictionary has a key (email address) which does not end with .com 
    if k.endswith('.com') is False:
        #Delete the item (key:value pair) from the copied dictionary.
        del dict2[k]
        print(dict2)
#Convert the dictionary to list to look up an item by an integer index.
name_list = list(dict2.values())
address_list = list(dict2.keys())

#Login to the ZJU email server
print("\n\nLogin to ZJU Mail to send an email")
sender_name = input("\tName:")
sender_email = input("\tEmail:")
password = input("\tPassword:")
server = smtplib.SMTP('smtp.zju.edu.cn', 25)
server.login(sender_email, password)

i = 0
for i in range (len(dict2)):
    count_receiver = name_list[i]
    count_address = address_list[i]
    print("The email has been sent to " +address_list[i])
    text = open('body.txt', 'r')
    text_open = text.read()
    #To address the email recipient by name, the word "user" from body.txt needs to be replaced
    change_username = re.sub(r"User",count_receiver, text_open)
    message = MIMEMultipart()
    message['From'] = sender_name
    message['Subject'] = "Dear " +count_receiver + ", Your Analysis Job Has Been Completed"
    message.attach(MIMEText(change_username, 'plain'))
    server.sendmail(sender_email, count_address, message.as_string()) 
    i = i + 1