'''
Created on 19-Mar-2018

@author: Titan
'''

import facebook
from setuptools import setup
from facepy import GraphAPI
from facepy.exceptions import *
import sqlite3, time



def getGroupMembers(group_id,access_token):
    graph = GraphAPI(access_token)
    data = graph.get(group_id + "/members")
    #print(data)
    
    for i in data['data']:
        d =i['name'],i['id']
        print(d)
        print(type(d))
    
    db =  sqlite3.connect("Group.db")
    c = db.cursor()
    c.execute("""DROP TABLE OldGroupTB""")
    
    c.execute("""ALTER TABLE NewGroupTB RENAME TO OldGroupTB""");
    
    c.execute("""CREATE TABLE NewGroupTB(MNo INTEGER PRIMARY KEY, name VARCHAR(25) NOT NULL, Mid VARCHAR(25) NOT NULL)""")

    for i in data['data']:
        d =i['name'],i['id']
        c.execute('INSERT INTO NewGroupTB(name,Mid) VALUES(?,?)',d)
        db.commit()  
        
    
    
def viewTBByName(TBName):
    db =  sqlite3.connect("Group.db")
    c = db.cursor()
    c.execute("SELECT * FROM "+TBName)
    print(c.fetchall())
    
def TestProject():
    db =  sqlite3.connect("Group.db")
    c = db.cursor()
    
    c.execute("SELECT name,Mid FROM NewGroupTB")
    table1 = c.fetchall()
    
    c.execute("SELECT name,Mid FROM OldGroupTB")
    table2 = c.fetchall()
    
    x = set(table1)
    x1 = set(table2)
    
    result = x.symmetric_difference(x1)
    differences = list(result)
    
    if len(differences) == 0:
        print("No new members added or left the group")
    else:
        
        
        #print(differences)

        for mem in differences:
            #print(mem[1] + " MemberID: " + mem[2] + " left the group")
            mid = mem[1]
            #print("mid: " + mid)
            for id in table1:
                MID = id[1]
                #print("MID: " + MID)
                if mid ==MID:
                    print(mem[0] + " MemberID: " + mem[1] + " new member added to the group")
        
            for n in table2:
                mmid = n[1]
                if mid == mmid:
                    print(mem[0] + " MemberID: " + mem[1] + " left the group")





group_id = ""
access_token = ""



if __name__ == '__main__':
    TestProject()



'''
graph = GraphAPI(access_token)
data = graph.get(group_id + "/members")

print(data['data'])
print(type(data['data']))

lst = []
    
for dd in data['data']:
    d = dd['name']
    lst.append(d)

print(lst)
print(type(lst))    
'''    




#getGroupMembers(group_id,access_token)
#viewTB()
#viewTBByName("NewGroupTB")
#viewTBByName("OldGroupTB")
 
#TestProject()

#122075815230302?fields=feed{message,comments},posts{feed_targeting,comments}

    
    


    


    
    



