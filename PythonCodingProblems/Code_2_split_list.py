import sys
from itertools import islice 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        print("The input parameter list is:{}",nums)
        pivot_prev_total=0;
        pivot_after_total=0;
        pivot_index=-1
        for i in range (0,len(nums)):
            print(i)
            first_list_range=i+1
            second_list_range=len(nums)-(i+1)
            length_to_split=[first_list_range,1,second_list_range]
            # Using islice 
            Inputt = iter(nums) 
            Output = [list(islice(Inputt, elem))for elem in length_to_split]
            print(Output)  
            pivot_prev_total=sum(Output[0])
            print("The previous total is: {} ",pivot_prev_total)
            pivot_after_total=sum(Output[2])
            print("The after pivot total is: {}",pivot_after_total)
            if pivot_prev_total==pivot_after_total:
                pivot_index=i
                
        return pivot_index
    
    
    
def main():
    
    x=Solution(z1)
    
    # creating an empty list 
    lst = [] 

    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 

    # iterating till the range 
    for i in range(0, n): 
        ele = int(input())
    	lst.append( ele )	
    print(lst) 


    
    pivot=x.pivotIndex(lst)
    print("The pivot index is {}", pivot)
        
        
    if __name__==main():
        main()
        