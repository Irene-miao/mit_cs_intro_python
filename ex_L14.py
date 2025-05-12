# -*- coding: utf-8 -*-
"""
Created on Tue May  6 15:17:39 2025

@author: meow

SOLUTION 1:
   
def keys_with_value(aDict, target):
 target_keys = [] 
for i in aDict.keys(): 
if aDict[i] == target:
 target_keys.append(i)
 target_keys.sort() 
return target_keys 


SOLUTION 2:
    
def all_positive(d):
 L = [] 
for k,v in d.items(): 
if sum(v) > 0: 
L.append(k) 
return sorted(L)
"""

def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    # Your code here  
    list = []
    for k, v in aDict.items():
        if v == target:
            list.append(k)
    return list

# Examples:
aDict = {1:2, 2:4, 5:2}
target = 2   
print(keys_with_value(aDict, target)) # prints the list [1,5]



def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a 
    positive value.
    """
    # Your code here  
    list = []
    
    for k, v in d.items():
        sum = 0
        for el in v:
            sum = sum + el
        if sum > 0:
            list.append(k)
    list.sort()
    return list
        
        

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]
