# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:29:02 2020

@author: deepa
"""


def split_list_sentences(sentence):
    print("The parameter passed was: \n")
    print(s)
    print("\n\nPrinting individual sentences of the same list: \n")
    l=[]
    for i in s:
        l.append(i)
        print(i)
    print("\n\nCapturing individual sentences in list 'l' and printing them:\n")
    for i in range(0,len(l)):
        print(l[i])
    print("\n\nCapturing individual words and printing them using the split function:")
    j=[]
    wholelist=[]
    for i in range(0,len(l)):
        #j=list(l[i])
        print(l[i].split())
        j.append(l[i].split())
        #j.append(l[i])
        #wholelist.append(j)
        #print(j)
    print(j)
    print("\nList of individual characters: \n")
    
        
        
        
    
    
    
    
    
    
    
    
    
    
    
s=["She sells sea shells on the seashore","Honesty is the best Policy","A stitch in time saves nine"] 
split_list_sentences(s)   