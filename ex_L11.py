# -*- coding: utf-8 -*-
"""
Created on Mon May  5 16:17:14 2025

@author: meow

SOLUTION:
    
def remove_and_sort(Lin, k): 
if len(Lin) <= k:
 Lin.clear() 
return 
for i in range(k): 
del(Lin[0])
 Lin.sort()    
    
"""

def remove_and_sort(Lin, k):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    # Your code here  
    if len(Lin) <= k:
        Lin.clear()
        
    for i in range(k):
        del Lin[i]
        
    Lin.sort()
    

    

# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]