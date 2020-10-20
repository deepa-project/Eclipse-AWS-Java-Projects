# -*- coding: utf-8 -*-
"""
"Daily Coding Problems" by Alex Miller, Lawrence Wu
Chapter 7:Binary Search Trees
Created on Mon Aug 10 04:22:08 2020
@author: deepa

"""
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        
class BST:
    def __init__(self):
        self.root=None

    def insert(self,x):
        if not self.root:
            self.root=Node(x)
        else:
            self._insert(x,self.root)
            
    def _insert(self,x,root):
        if x<root.data:
            if not root.left:
                root.left=Node(x)
            else:
                self.insert(x,root.left)
                
        else:
            if not root.right:
                root.right=Node(x)
            else:
                self.insert(x,root.right)
                
    def find(self,x):
        if not self.root:
            return False
        else:
            return self._find(x,self.root)
    
    def _find(self,x,root):
        if not root:
            return False
        elif x==root.data:
            return True
        elif x<root.data:
            return self._find(x,root.left)
        else:
            return self._find(x,root.right)
        
    def main():
        xBinary=BST
        xBinary.insert(10,100)
        xBinary.insert(20,10)
        xBinary.insert(30,10)
        xBinary.insert(-9,10)
        xBinary.insert(-6,10)
        xBinary.insert(9,10)
        xBinary.insert(3,10)
        print(xBinary)
        

    if __name__=="__main__":
        main()        
        
        
        
    
        



                    
                
                
                
            
            
            
            
        


