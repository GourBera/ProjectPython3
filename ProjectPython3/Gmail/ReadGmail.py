'''
Created on May 22, 2018

@author: berag
'''
import smtplib
import time
import imaplib
import email


emailID = '@gmail.com'
emailPass = ''

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(emailID, emailPass)
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

result, data = mail.search(None, "ALL")
#print(data)
ids = data[0] # data is a list.
id_list = ids.split()

for i in id_list:
    result, data = mail.fetch(i, "(RFC822)") # fetch the email body (RFC822) for the given ID
    raw_email = data[0][1] # here's the body, which is raw text of the whole email
    # including headers and alternate payloads
    #print(raw_email)
    data = str(raw_email)
    #print(data)

    b = data.find("Subject: ")
    print(data[b+9:])

''' 
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest

result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
raw_email = data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads
print(raw_email)
'''
'''
result, data = mail.uid('search', None, "ALL") # search and return uids instead
latest_email_uid = data[0].split()[-1]
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
raw_email = data[0][1]

data = str(raw_email)
print(data)

b = data.find("Subject: ")
print(data[b+9:])
'''

