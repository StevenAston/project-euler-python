# -*- coding: utf-8 -*-
"""
Created on Sun May 14 01:17:34 2017

@author: Steven
"""
from functools import reduce
import time
tStart = time.time()

def gcd(a,b):
    """Return greatest common divisor"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple"""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args.""" 
    return reduce(lcm, args)
for i in range(20,200):
    tStart = time.time()
    print(lcmm(*range(1, i)))
    print(i, " run time = " + str((time.time() - tStart)))

tStart = time.time()
def delbart(t,n):
    if n > 0:
        if not (t%n):
            if delbart(t, n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

i = 20
while not delbart(i,20):
    i +=20

print (i)
print("run time = " + str((time.time() - tStart)))