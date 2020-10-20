# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 06:11:49 2020

@author: deepa
"""
#Daily Coding Problems-Alex Miller,Lawrence Wu
# locate smallest window in an array to be sorted
#bounds-indices of the lowest and highest elements in a sorted array
#Example: given x=[3,7,5,6,9]]
#sortedX=[3,5,6,7,9]---first and last elements remain the same=>[3,-,-,-,9]
#that is x[0] andx[4] remain unchanged-so the to be sorted window
# is actually [x[[1],x[2],x[3]]]--so lower bound is 1, upper bound is 3
#Program must return (1,3)
def window(array):
    left,right=None,None
    s=sorted(array)
    for i in range(len(array)):
        if array[i]!=s[i] and left is None:
            left=i
        elif array[i]!=s[i]:
            right=i
    return left,right

def display(nums,x):
        for i in range(0,(x-1)):
            print(nums[i])
          
def main():
        print("Enter the number of integers:\n")
        n=int(input("Number of elements"))
        arrayX=[]
        print("Enter the integers of the array")
        for i in range(0, n):
            arrayX.append(int(input()))
       
        result=window(arrayX)
        print(result)
        print(type(result)) 
if __name__ == "__main__":
    main()            
