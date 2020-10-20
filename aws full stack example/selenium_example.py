# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:39:25 2020

@author: deepa
selenium exercise
"""

#importing webdriver from selenium 
from selenium import webdriver 

#selecting Firefox as the browser 
#in order to select Chrome 
# webdriver.Chrome() will be used 
driver = webdriver.Firefox(executable_path = '/path/to/geckodriver') 

#URL of the website 
url = "https://www.geeksforgeeks.org/"

#opening link in the browser 
driver.get(url) 

