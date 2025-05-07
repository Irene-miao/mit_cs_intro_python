# -*- coding: utf-8 -*-
"""
Created on Sat May  3 16:05:31 2025

@author: meow

SOLUTION:
     
def all_true(n, Lf):
 flag = 
True 
for f in Lf: 
if not f(n):
 flag = 
False 
break 
return flag
    
"""


def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Your code here
    for f in Lf:
        if f(n):
            return True

    return False
    

# Examples:    
all_true() # prints 6
