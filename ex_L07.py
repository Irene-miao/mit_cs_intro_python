# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 15:30:44 2025

@author: meow
"""

def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic a×x² + b×x + c.
    """
    # Your code here
    result = (a*x**2) + (b*x) + c
    return result

# Examples:    
print(eval_quadratic(1, 1, 1, 1)) # prints 3


def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    Prints the sum of the two evaluations. Does not return anything.
    """
    # Your code here
    result = (a1*x1**2) + (b1*x1) + c1
    result2 = (a2*x2**2) + (b2*x2) + c2
    print(result+result2)

# Examples:    
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) # prints 6
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6 then None
