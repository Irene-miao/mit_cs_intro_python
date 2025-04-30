# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 14:33:24 2025

@author: meow

Finger Exercise Lecture 6:
Assume you are given an integer 0 <= N <= 1000. 
Write a piece of Python code that uses bisection search to guess N.
 The code prints two lines: count: with how many guesses it took to find N, 
 and answer: with the value of N. Hints: If the halfway value is exactly in 
 between two integers, choose the smaller one.
 
 SOLUTION:
     low = 0 
high = 1001 
guess = (high+low)//2 
count = 1 
while guess != N: 
if guess < N:
 low = guess 
elif guess > N:
 high = guess
    guess = (high+low)//2
 count += 
1 
print("count:",count) 
print("answer:",guess) 

"""


low = 0
high = 1000
count = 0
answer = ''
N = 1001

while low <= high:
    mid_point = (low+high)//2
    if N == mid_point:
       answer = N
       print("Answer: ",answer)
       print("Count ",count)
       break
    elif N > mid_point:
        low = mid_point
        count += 1
    elif N < mid_point:
        high = mid_point
        count+=1
    else:
        print("not found")



