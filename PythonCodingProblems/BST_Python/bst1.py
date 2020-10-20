"""
Source:Data Structure and algorithmic Thinking with Python-Narasimha Karumanchi
Careermonk.com

Program:Binary Tree class and methods


"""
class BinaryTreeNode:
	def __init__(self,data):
		self.data= data #root node
        
		self.left=None  #left child
		self.right=None #right child
          
        
        
   
        
        
        
     
       
        
def main():        
    print("Main function:")
    data=3
    x=BinaryTreeNode(data)
    print(data)
    print(x.data)
    
    print(x.left)
    print(x.right)
    x.printNode()
    
    
    
    
main()    
	  			
		