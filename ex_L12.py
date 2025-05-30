# -*- coding: utf-8 -*-
"""
Created on Tue May  6 15:17:39 2025

@author: meow
"""

def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    # Your code here
    copy = nums_list[:]
    number = []
    for c in copy:
        for el in nums_list:
            if c**2 == el:
                number.append(c)
    return len(number)

# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3