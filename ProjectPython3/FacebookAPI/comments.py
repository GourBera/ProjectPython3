'''
Created on 20-Mar-2018

@author: Titan
'''

if __name__ == '__main__':
    pass

import facebook
from setuptools import setup
from facepy import GraphAPI
from facepy.exceptions import *
import urllib3, urllib

str = ""



access_token = ""
group_id = ""
statusid = ""

graph = GraphAPI(access_token)
data = graph.get(group_id + "/members")
print(data)

graph = facebook.GraphAPI(access_token)
    
graph.put_object(statusid, "comments", message="test comment!")
print("commented!")






















