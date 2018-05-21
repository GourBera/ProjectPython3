'''
Created on Mar 13, 2018
@author: berag

SQLite database with Python – Simple Server Authentication and data insertion 

'''

import sqlite3, time

''' 
cursor.execute("""CREATE TABLE IF NOT EXISTS studentTB(sID INTEGER PRIMARY KEY,uname VARCHAR(25) NOT NULL,mailID VARCHAR(25) NOT NULL,password VARCHAR(25) NOT NULL);""")
cursor.execute("""INSERT INTO studentTB(uname,mailID,password) VALUES("Gour","gour.b@gmail.com","pwd1")""")
db.commit()

cursor.execute("SELECT * FROM studentTB")
print(cursor.fetchall())

'''

def viewDB():
    with sqlite3.connect("studentDB.db") as db:
        c = db.cursor()
        c.execute("SELECT * FROM studentTB")
        print(c.fetchall())


def addusers():    
    found = 0    
    while found == 0:
        uname = input("Pease Enter user name: ")
        with sqlite3.connect("studentDB.db") as db:
            c = db.cursor()
        
        find_user = ("SELECT * FROM studentTB WHERE uname = ?")
        c.execute(find_user,[(uname)])
        
        if c.fetchall():
            print("user already exist, try another!!!")
        else:
            uname = input("Enter Name: ")
            mailID = input("Enter Email ID: ")
            password = input("Enter Password: ")
            passwordAgain = input("Enter Password: ")
    
            if password != passwordAgain:
                print("password does not match, try again!!!")
                password = input("Enter Password: ")
                passwordAgain = input("Enter Password: ")
        
            found = 1
        
    insertData = """INSERT INTO studentTB(uname,mailID,password) VALUES(?,?,?)"""
    c.execute(insertData,[(uname),(mailID),(password)])
    db.commit()
        
    
    print("Student ID created successfully!!!")
    again = input("Do you want to add another users ?(y/n): ")
    if again.lower() == "n" or again.upper() == "N":
        print("Good Bye")
        time.sleep(2)               
    else:
        addusers()
    

def login():
    while True:
        mailID = input("Please Enter your Mail ID: ")
        password = input("Please Enter your password: ")
        
        with sqlite3.connect("studentDB.db") as db:
            c = db.cursor()
            find_user = ("SELECT * FROM studentTB WHERE mailID = ? AND password = ?")
            c.execute(find_user,[(mailID),(password)])
        
            result = c.fetchall()
        
            if result:
                for i in result:
                    #Second column name
                    print("Welcome "+i[1] + ". login successful") 
                break
            else:
                print("User name or password is incorrect")
                again = input("Do you want to retry ?(y/n): ")
            
                if again.lower() == "n" or again.upper() == "N":
                    print("Good Bye")
                    time.sleep(2)
                else:
                    login()
                    
                    
                    
                    

if __name__ == '__main__':
    viewDB()            
    addusers()            
    login()
 

