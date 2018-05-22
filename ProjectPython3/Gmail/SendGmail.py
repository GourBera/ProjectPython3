'''
Created on May 22, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

import smtplib


def sendGmail(TO, SUBJECT, TEXT, gmail_sender, gmail_passwd):    

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print('email sent')
    except:
        print('error sending mail')

    server.quit()
    
TO = 'incidntmgmt@gmail.com'
SUBJECT = 'Site'
TEXT = """https://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/"""
gmail_sender = '@gmail.com'
gmail_passwd = ''

sendGmail(TO, SUBJECT, TEXT, gmail_sender, gmail_passwd)