'''
Created on 23-Mar-2018

@author: Titan
'''
from flask import Flask
import requests



if __name__ == '__main__':
    resp = requests.get('https://firestore.googleapis.com/************/users/userdoc/')
    print(resp)


