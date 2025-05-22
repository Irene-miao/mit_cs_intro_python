# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:42:23 2025

@author: meow

Solution:
    
 class Container(object):
 def __init__(self):
        self.myList = []
 def size(self):
 return len(self.myList)
 def add(self, elem):
        self.myList.append(elem)
 class Queue(Container):
 def remove(self):
 if self.size() > 0:
 return self.myList.pop(0)
 return None
    
"""

class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        # Your code here
        return len(self.myList)

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        # Your code here
        self.myList.append(elem)

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        # Your code here
        
        if len(self.myList) > 0:
            elem = self.myList.pop(0)
            return elem
        return None
        
        
q = Queue()
q.add(1)
q.add(2)
q.add(3)
print(q.size())
elem = q.remove()
q.remove()
q.remove()
print(elem)
empty = q.remove()
print(empty)
print(q.size())     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        