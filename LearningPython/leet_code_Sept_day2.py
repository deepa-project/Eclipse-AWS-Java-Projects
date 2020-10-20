# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Solution:
    def containsearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] is not None and nums[j] is not None:
                    print(int(nums[i]-nums[j]),i-j,t,k)
                
                    
                    if abs(int(nums[i]-nums[j]))<=t:
                        if abs(i-j)<=k:
                            return 1
        return 0
    
def main():
        x =Solution()
        t=int(input("Enter t:"))
        k=int(input("Enter k:"))
        n=int(input("Enter the number of integers in the list:"))
        print("Enter the integers :")
        int_list=[]
        for i in range(0,n):
            int_list[i]=int_list.append(int(input()))
        
      
        result=x.containsearbyAlmostDuplicate(int_list,k,t)
        print("Result=",result)
        
if __name__=="__main__":
        main()
 