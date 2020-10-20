class Solution:
    def getHint(self, secret: str, guess: str) -> str:
    	ls=list(secret)
    	print(ls)
    	ls2=list(guess)
    	print(guess)
    	for i in ls:
    		for j in ls2:
    			if ls[i]==ls2[i]:
    				then ls=ls.replace(ls[i],'A')
    			elif ls[i]==ls2[j] and i!=j:
    				then ls=ls.replace(ls[i],'B')
    	returnSTR=""		
    return returnSTR.join(ls)			






def main():
	secret=str(input("Enter your secret number"))
	guess=str(input("Enter your guess number"))
	print("The string to be searched is "+secret)
	print("The string that was guessed is "+guess)
	abc=getHint(secret,guess)
	print(abc)






if __name__=="main":
	main()
