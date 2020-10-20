#Daily Coding Problem -Alex Miller and Lawrence Wu
#Maximum Sub array sum
#Find the maximum sum of any continuous sub array of the array
#Example: arrayX=[a,b,c,d,e]
#The various sums are a,b,c,d,e,a+b,a+b+c,a+b+c+d,a+b+c+d+e,b+c,
#b+c+d,b+c+d+e,c+d,c+d+e,c+d+e+a,d+e,d+e+a,e+a
# The function needs to find and return the maximum of the above values
def max_subarray_sum(arr):
    max_ending_here=max_so_far=0
    for x in arr:
        max_ending_here=max(x,max_ending_here+x)
        max_so_far=max(max_so_far,max_ending_here)
    return max_so_far
def min_subarray_sum(arr):
    min_ending_here=min_so_far=0
    
    for x in arr:
        min_ending_here=min(x,min_ending_here+x)
        min_so_far=min(min_so_far,min_ending_here)
    return min_so_far   

def maximum_circular_subarray(arr):
    max_subarray_sum_wraparound=sum(arr)-min_subarray_sum(arr)
    return max(max_subarray_sum(arr),max_subarray_sum_wraparound)     

def display(arr,n):
    for i in range(0,n):
        print(arr[i])
        
def main():
     print("Enter the number of elements\n")
     x=int(input("Number of Elements"))
     arrayX=[]
     print("Enter the elements:")
     for i in range(0,x):
         arrayX.append(int(input()))
     display(arrayX,x) 
     sum_Y=max_subarray_sum(arrayX) 
     print("Max subarray sum is :=")
     print(sum_Y)
      
     
if __name__=="__main__":
    main()     
                         
         
           
        

