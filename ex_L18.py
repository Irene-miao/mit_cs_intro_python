# -*- coding: utf-8 -*-
"""
Created on Tue May 13 19:58:05 2025

@author: meow

SOLUTION:
    
class Circle():
 def __init__(self, radius):
   self.r = radius
 def get_radius(self):
 return self.r
 def __add__(self, c):
 return Circle(self.r + c.r)
 def __str__(self):
 return str(self.r)    
"""

class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        # your code here
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        # your code here
        return self.radius

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        # your code here
        return self.radius+c.get_radius()

    def __str__(self):
        """ A Circle's string representation is the radius """
        # your code here
        return "Circle's radius: "+ str(self.radius)
    
c = Circle(5)
c1 = Circle(1)
c2 = c+c1
print(c2)