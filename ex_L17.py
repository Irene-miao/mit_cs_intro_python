# -*- coding: utf-8 -*-
"""
Created on Mon May 12 19:39:38 2025

@author: meow

SOLUTION:

 class Circle():
 def __init__(self, radius):
   self.r = radius
 def get_radius(self):
 return self.r
 def set_radius(self, radius):
   self.r = radius
 def get_area(self):
 return 3.14*self.r*self.r 
def equal(self, c):
 return (c.r == self.r)
 def bigger(self, c):
 if c.r > self.r:
 return c
 elif c.r < self.r:
 return self
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

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        # your code here
        self.radius = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        # your code here
        return (self.radius**2)*3.14

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        # your code here
        
        c_radius = c.get_radius()
        if self.radius == c_radius:
            return True
        else: 
            return False
        

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        # your code here
        if self.radius > c.get_radius():
            return self
        else: 
            return c
        
big_circle = Circle(10)
small_circle = Circle(5)     
small_circle.set_radius(3)
print(big_circle.get_area())
print(small_circle.get_area())
print(big_circle.equal(small_circle))
print(small_circle.bigger(big_circle))