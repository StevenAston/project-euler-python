# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:43:44 2017

@author: Steven
"""

def findFibonnacciUnderX(x):
    a = 0
    b = 1
    c = 1
    sum = 0
    while b < x:
        if b % 2 == 0:
            print("Adding even Fibbonacci term", b)
            sum += b
        c = a + b
        a = b
        b = c
    return sum
        
print("Sum =",findFibonnacciUnderX(4000000))