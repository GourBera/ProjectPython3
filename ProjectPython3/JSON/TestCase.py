'''
Created on Mar 8, 2018

@author: berag
'''
'''
Convert xml to json
'''
#pip install xmltodict

import json
import xmltodict
 
with open("C:\\Users\\berag\\Desktop\\XMLtoJSON\\xml.xml", 'r') as f:
    xmlString = f.read()
 
print("XML input (sample.xml):")
print(xmlString)
     
jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
 
print("C:\\Users\\berag\\Desktop\\XMLtoJSON\\output(output.json):")
print(jsonString)
 
with open("C:\\Users\\berag\\Desktop\\XMLtoJSON\\output.json", 'w') as f:
    f.write(jsonString)