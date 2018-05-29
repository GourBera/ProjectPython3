'''
Created on May 29, 2018

@author: berag
'''
import os

print('Current directy: ', os.getcwd())


def rename_files(source, dest):
    file_list = os.listdir(source)
    dir = os.getcwd()
    os.chdir(source)
    
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    
    os.chdir(dir)






if __name__ == '__main__':
    rename_files()












