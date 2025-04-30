# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 19:45:38 2025

@author: meow

SOLUTION:
i = 1 
while i**3 < N:
 i += 
N 
is
 
not
 
a
 
perfect
 
cube.
 
Hint:
 
1 
if i**3 == N: 
print(i) 
else: 
print('error')

"""

# Finger Exercise Lecture 04

N = 25
found = False

for n in range(1, N):
    if n**3 == N:
        found = True
        print(n)
        
if not found:
    print("error")