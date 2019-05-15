# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:00:58 2019

@author: Adele
"""

import re
import copy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#open address_information.csv
#'with open' will close the file automatically
with open('address_information.csv', 'r') as address_book:
#read the info in the csv file
    address_open = address_book.read()


#CHECK THE VALIDITY OF EMAIL ADDRESS------------------------

#find all email addresses in the excel file.
valid_address = re.findall (r"[\w\-.]+@[\w\-.]+", address_open)
#extract all email RECIPIENTS in the excel file.
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
        #Print the result of address validation (wrong)
        print(k,': Wrong address!')
        #Delete the item (key:value pair) from the copied dictionary.
        del dict2[k]
    else:
        #if ends with .com, then it is a valid email address
        print(k,': Correct address!')
        

#Convert the dictionary to list to look up an item by index.
name_list = list(dict2.values())
address_list = list(dict2.keys())



#SEND EMAILS----------------------------------------------

#Login to the ZJU email server
print("\n\nLogin to ZJU Mail")
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
    #Open body.txt to be used as the message in the email
    #'will open' automatically closes the file after use
    with open('body.txt', 'r') as text:
        text_open = text.read()
    
    #Modify the body info: to address the email recipient by name, the word "user" from body.txt needs to be replaced
    change_username = re.sub(r"User",count_receiver, text_open)
    message = MIMEMultipart()
    message['From'] = sender_name
    message['Subject'] = "To " +count_receiver + ", Your Analysis Job Has Been Completed"
    message.attach(MIMEText(change_username, 'plain'))
    server.sendmail(sender_email, count_address, message.as_string()) 
    i = i + 1