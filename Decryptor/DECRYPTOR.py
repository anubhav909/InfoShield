#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def decryption(message,passcode):
    org_msg=""
    for i in message:
        if(i in [' ','!','@','#','$','%','^','&','*','(',')','-','_','=','+','/','~','.']):
            org_msg += i
        if(i in map(str,list(range(0,10)))):
                org_msg+=chr(((ord(i)-passcode-48)%10)+48)
        if(i.isupper()):

                a=chr(((ord(i)-passcode-65)%26)+65)
                org_msg+=a
        if(i.islower()):
                a=chr(((ord(i)-passcode-97)%26)+97)
                org_msg+=a
    return(org_msg)

#output=decryption(encryption,int(input("Enter the password: ")))
#print(output)

