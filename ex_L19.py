# -*- coding: utf-8 -*-
"""
Created on Tue May 13 20:00:19 2025

@author: meow

SOLUTION:
class Container(object):
 def __init__(self):
        self.myList = []
 def size(self):
 return len(self.myList)
 def add(self, elem):
        self.myList.append(elem)
 class Stack(Container):
 def remove(self):
 if self.size() > 0:
 return self.myList.pop()
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
    
    def __str__(self):
        return str(self.myList)

class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed
        Returns the element removed or None if the queue contains no elements
        """
        # Your code here
        if len(self.myList) == 0:
            return None
        else:
            print(f'list: {self.myList}')
            element =   self.myList.pop(-1)
            print(f'el: {element}')
            return element
        
c = Container()
print(f'c: {c}')
c.add(2)
c.add(5)
c.add(10)
print(f'c after: {c}')
s = Stack()
s.add(1)
s.add(2)
s.add(3)
print(f's before: {s}')
element = s.remove()
print(f's after: {s}')
print(f'element: {element}')
        
        
        
        
        
        
        