'''
Created on May 21, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")


driver.execute_script("myFunction()")
elm = driver.find_element_by_xpath("xpath")
driver.execute_script("arguments[0].setAttribute('style', Arguments[1]);", elm, "color: red, border: 3px solid red;")



