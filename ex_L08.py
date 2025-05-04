# -*- coding: utf-8 -*-
"""
Created on Sat May  3 15:43:52 2025

@author: meow

SOLUTION:
    
def same_chars(s1, s2): 
for i in s1: 
if i not in s2: 
return False 
for i in s2: 
if i not in s1: 
return False 
return True 

"""


def same_chars(s1, s2):
 """
 s1 and s2 are strings
 Returns boolean True is a character in s1 is also in s2, and vice 
versa. If a character only exists in one of s1 or s2, returns False.
 """
 # Your code here 
 
 count = 0
 for char in s1:
     if char not in s2:
         count += 1
 
 for c in s2:
     if c not in s1:
         count =+ 1
 
 if count > 0:
    return False
 else:
    return True
 
# Examples: 
print(same_chars("abc", "cab")) # prints True 
print(same_chars("abccc", "caaab")) # prints True 
print(same_chars("abcd", "cabaa")) # prints False 
print(same_chars("abcabc", "cabz")) # prints False
