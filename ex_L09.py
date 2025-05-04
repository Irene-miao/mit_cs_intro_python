# -*- coding: utf-8 -*-
"""
Created on Sat May  3 15:43:38 2025

@author: meow

SOLUTION: 
    
def dot_product(tA, tB): 
tot = 0 
for i in range(len(tA)):
 tot += tA[i]*tB[i] 
return (len(tA), tot)


"""

def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where:
    * the first element is the length of one of the tuples
    * the second element is the sum of the pairwise products of tA and tB
    """
    length = len(tA)
    total = 0  # Avoid using "sum" as a variable name since it's a built-in function

    i = 0
    while i < length:
        total += tA[i] * tB[i]
        i += 1

    return (length, total)



# Examples: 
tA = (1, 2, 3) 
tB = (4, 5, 6) 
print(dot_product(tA, tB)) # prints (3,32)