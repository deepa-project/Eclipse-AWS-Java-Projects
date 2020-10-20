#Daily Coding Problems-Alex Miller,Lawrence Wu
#given an array of integers, [a,b,c,d]->return a new array[x1,x2,x3,x4] 
#such that each elemnt i in the new array is the product of all the elements 
#except the integer in the ith position->[bcd,acd,abd,abc]
import sys
def product(nums):
    #Generate prefix products
    prefix_products=[]
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1]*num)
        else:
            prefix_products.append(num)
            
    #Generate suffix products.
    suffix_products=[]
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1]*num)
        else:
            suffix_products.append(num)
    suffix_products=list(reversed(suffix_products))
    
    #Generate result from the product of prefixes and suffixes
    result=[]
    for i in range(len(nums)):
        if i==0:
            result.append(suffix_products[i+1])
        elif i==len(nums)-1:
            result.append(prefix_products[i-1])
        else:
            result.append(
                prefix_products[i-1]*suffix_products[i+1])
    return result
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
        arrayY=[]
        arrayY=product(arrayX)
        display(arrayY,n)
if __name__ == "__main__":
    main()     
        
        
            
        