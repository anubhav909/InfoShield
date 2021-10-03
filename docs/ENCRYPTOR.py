#!/usr/bin/env python
# coding: utf-8

# In[58]:


def cyphar_encryption(message,shift):
    hide=""
    for i in message:
        if(i in [' ','!','@','#','$','%','^','&','*','(',')','-','_','=','+','/','~','.']):
            hide += i
        if(i.isupper()):
                h=chr(((ord(i)+shift-65)%26)+65)
                hide+=h
        if(i in map(str,list(range(0,10)))):
                hide+= chr(((ord(i)+shift-48)%10)+48)
        if(i.islower()):
                h=chr(((ord(i)+shift-97)%26)+97)
                hide+=h
    return(hide)


# encryption=cyphar_encryption(message,int(input("Enter the password: ")))
# print(encryption)


# In[5]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# In[1]:


def mail(sender,reciever,message,password   ):
    fromaddr=sender
    toaddr=reciever
    msg= MIMEMultipart()

    msg['From']=fromaddr
    msg['To']=toaddr
    msg['Subject']= 'Your Encrypted File.'
    body=message
    msg.attach(MIMEText(body,'plain'))
    # s=smtplib.SMTP('smtp.gmail.com',587)
    s=smtplib.SMTP_SSL('smtp.googlemail.com',465)
    s.login(fromaddr,password)
    text=msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()
    return 1

