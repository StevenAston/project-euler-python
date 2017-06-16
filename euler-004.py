# -*- coding: utf-8 -*-
"""
Created on Sun May 14 01:17:34 2017

@author: Steven
"""

import time

def isPalindrome(x):
    string = str(x)
    if string == string[::-1]:
        return True
    else:
        return False

largestPalindrome = 9009
tStart = time.time()

for a in range(888,999):
    for b in range(888,999):
        if isPalindrome(a*b):
            if (a*b) > largestPalindrome:
                largestPalindrome = a*b
                
print(largestPalindrome)
print("run time = " + str((time.time() - tStart)))