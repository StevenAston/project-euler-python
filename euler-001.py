# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:32:08 2017

@author: Steven
"""

def checkMultiple(x):
    if x % 5 == 0 or x % 3 == 0:
        return True
    else:
        return False

def findandSumMultiplesBelowN(n):
    sum = 0
    for i in range(1,n):
        if checkMultiple(i) == True:
            sum += i
    return sum


print (findandSumMultiplesBelowN(1000))