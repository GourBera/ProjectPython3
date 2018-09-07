'''
Created on 12-Mar-2018

@author: Titan
'''

if __name__ == '__main__':
    pass


import sqlite3
data_person_name = [('Michael', 'Fox'),
                    ('Adam', 'Miller'),
                    ('Andrew', 'Peck'),
                    ('James', 'Shroyer'),
                    ('Eric', 'Burger')]

con = sqlite3.connect(":memory:")
c = con.cursor()

c.execute('''CREATE TABLE q1_person_name
             (name_id INTEGER PRIMARY KEY,
              first_name varchar(40) NOT NULL,
              last_name varchar(20) NOT NULL)''')
c.executemany('INSERT INTO q1_person_name(first_name, last_name) VALUES (?,?)', data_person_name)

for row in c.execute('SELECT * FROM q1_person_name'):
    print(row)