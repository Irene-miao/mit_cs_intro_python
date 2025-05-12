# -*- coding: utf-8 -*-
"""
Created on Fri May  9 19:08:55 2025

@author: meow

SOLUTION:
    
def flatten(L):
result = [] 
for i in L: 
if type(i) == list:
 result.extend(flatten(i)) 
else:
 result.append(i) 
return result
"""

def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    # Your code here  
    if len(L) == 1:
        # only one element in list, return it
        if type(L[0]) != list:
            return L
        else:
            # first element is a list, flatten it
            return flatten(L[0])
    else:
        # more than 1 list in list, first element is int, add to flatten remaining elements
        if type(L[0]) != list:
            return [L[0]]+ flatten(L[1:])
        else:
            # first element is a list, flatten it and add to flatten remaining elements
            return flatten(L[0])+flatten(L[1:])
    

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]