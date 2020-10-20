# -*- coding: utf-8 -*-
#'Daily Coding Problem' Alex Miller,Lawrence Wu
"""
Created on Thu Aug  6 20:50:45 2020

@author: deepa
"""
#Reverse a linked list

#linked list= 1-->2-->3-->4
#Result required is 1<--2<--3<--4
#Web Source:https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python
#Difficulty_Program Solution in book plays with only nodes of a linkedlist, not 
#a linkedlist--Node is data type for a linkedlist class--keyword is 'self'

class Node:
    def  __init__(self,data,next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev
        
   # A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
    # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

def reverse(node):
    #_reverse() reverses and returns both head and tail.
    #Conventionally, an underscore denotes an unused variable
    
    head,_ =_reverse(node)
    return head

    

def _reverse(node):
    if node is None:
        return None,None
    
    if node.next is None:
        return node, node
    
def main():
    
    
    LL = LinkedList()
    LL.insert(3)
    LL.insert(4)
    LL.insert(5)
    LL.printLL()
    reverse(LL.head.data)
    LL.printLL()
    
if __name__=="__main__":
        main()    
        
    
    
    


