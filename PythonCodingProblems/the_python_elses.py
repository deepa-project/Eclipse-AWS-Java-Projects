# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:25:09 2020

@author: deepa
"""

sentence="this is a cutie pie"
def do_something_with(word):
    print("this function is called from the else of the if_else inside the for loop")
    print("This is just a pass function")
    pass
for word in sentence:
    if word=="quit":
        print ("Time to quit")
        break
    else:
        do_something_with(word)
        
else:
    print ("there was no 'quit' in the sentence")
    print("The above sentence is from the else of the for loop in python")
print ("Now w're done...")        