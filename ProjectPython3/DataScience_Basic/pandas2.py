'''
Created on May 11, 2018

@author: berag
'''
import pandas as pd
import numpy as np
import pandasql


'''
rdata = pd.read_csv("C:\\Users\\berag\\DataScience\\titanic-data.csv")

#print(data)
#print(data.describe())
#print(data[['Fare']].apply(np.mean))
#['Survived'],['Fare'],['Sex']
df = pd.DataFrame(data = rdata, columns=['Fare', 'Sex','Age','Survived'])
#print(df.describe())
#print(df)
#df['Age'] = df['Age'].fillna(df['Age'].mean())  #
#print(df)

df['Age'] = df['Age'].fillna(np.mean(df['Age']))

print(df)
print(np.sum(df['Age'])) 
print(np.mean(df['Age'])) 
'''

aadhaar_data = pd.read_csv("C:\\Users\\berag\\SampleProject\\DataScience\\aadhaar_data.csv")
aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

q = """ SELECT * FROM aadhaar_data LIMIT 50
    -- SQL Comment
    """
#aadhaar_solution = pandasql.sqldf(q.lower(), locals())
aadhaar_solution = pandasql.sqldf(q, globals())
b = pd.DataFrame(data = aadhaar_solution)
print(b)






