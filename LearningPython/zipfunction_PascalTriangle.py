# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:54:45 2020

@author: deepa
PascalTriangle_zip function :https://www.askpython.com/python/examples/pascals-triangle-using-python
"""

def PascalTriangle(n):
   trow = [1]
   y=[]
   for x in range(n):
      print(trow)
      trow=[left+right for left,right in zip(trow+y, y+trow)]
     
   return n>=1

n=int(input("Enter an integer value: "))
PascalTriangle(n)
