# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 05:21:45 2020

@author: deepa
"""
#Daily Coding Problems-Alex Miller,Lawrence Wu
#Find the number of smaller elements to the right
#Example, given array X=[3,5,7,2,1]
#For 3->the number of elements to its right which are kess than 3, that is(2,1
#) is 2,
#For 5, its again(2,1)->2,
#for 7, its again (2,1)->2:
#   For2, there is only one element right of it and is smaller to it->
#   Element =1, the nubmer of elements right of it smaller to 2 is 1
#for the last element, its always going to be 0 as there is no elmt to its rt
#Another example: for y=[4,2,7,5,9]
#the function must return z=[1,0,1,0,0,]

def number_of_elements_on_right(arrayX):
    result=[]
    for i,num in enumerate(arrayX):
        count=sum(val<num for val in arrayX[i+1:])
        result.append(count)
    return result

def display(arrayY):
#   for i in range(0,len(arrayY)):
#       print(arrayY[i])
    print(arrayY)    
        
def main():
    print("Enter the number of elements")
    num=int(input("Number of Elements = "))
    arrayX=[]
    print("Enter the elements")
    for i in range(0,num):
        arrayX.append(int(input()))
    print("The array you entered is :")
    display(arrayX)
    print("The array which shows the number of elements<i th elmnt's right")        
     
    arrayZ=[] 
    arrayZ=number_of_elements_on_right(arrayX)
    display(arrayZ)
                  
if __name__=="__main__":
    main()    
    
           


    
    
    


