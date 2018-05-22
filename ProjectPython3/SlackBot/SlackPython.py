'''
Created on 13-Mar-2018

@author: Titan
'''
from os import *
import os
import time
import requests
from slackclient import SlackClient
import sys
from slacker import Slacker
import json


slack = Slacker("xoxb-")
sc = SlackClient("xoxb-")

# Get All Channel
sc.api_call("channels.list", exclude_archived=1)

# Posting message in grneral
message = "Hello Everyone..!"
slack.chat.post_message("#general", message)


payload = {'token': 'xoxb-', 'user': 'Gour'}
r = requests.get("https://gour.slack.com/messages/*****/", params=payload)
print(r) #<Response [200]>

# Getting the message back that already posted
token = "xoxb-"  # found at https://api.slack.com/web#authentication
sc = SlackClient(token)
if sc.rtm_connect():  # connect to a Slack RTM websocket
    while True:
        print("You typed----  ")
        print(sc.rtm_read())  # read all data from the RTM websocket
        time.sleep(1)        
else:
    print('Connection Failed, invalid token?')



'''
data = r.json()
# unmarshal JSON to a dict
d = json.loads(data)

for i in d:
    print(i, d[i])
'''

#print(r.json)
#k = r.json
#for msg in k:
 #   print(msg)

'''
from slackclient import SlackClient

slack_token = os.environ['xoxb-']
sc = SlackClient(slack_token)

sc.api_call(
  "channels.list",
  exclude_archived=1
)
  
    
# get the correct channel id
for channel in channels['channels']:
    if channel['name'] == channel_name:
        channel_id = channel['id']
if channel_id == None:
    raise Exception("cannot find channel " + channel_name)

# get the history as follows: 
history = sc.api_call("channels.history", channel=channel_id)

# get all the messages from the history: 
messages = history['messages']

# Or reference them by ID, so in this case get the first message:
ids = messages[0]

'''







