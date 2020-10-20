class Solution:
    def maxProduct(self, nums) -> int:
        max=1
        for i in nums:
           
            j=i+1
            
            if j<len(nums) and nums[i]*nums[j]>max:
                max=nums[i]*nums[j]
            i=j
            #print("max=",max)
            
        return max  

def main():
	lst=[]
	#print("line1")
	print("New code:Enter the number of integers:")
	#print("line2")
	n=0
	n=int(input())
	#print("line3")
	#print(n)
	#print("line4")
	
	print("Enter the integers:")
	#print("line5")
	for i in range(0,n):
		#print(i)
		lst.append(int(input()))
		#print(lst[i])

	#print("line6")
	x=Solution().maxProduct(lst)
	#print("line7")
	print(x)
	#print("line8")

if __name__=="__main__":
	#print("line9")
	main()   


        