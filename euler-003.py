# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:59:16 2017

@author: Steven
"""
import math

def findPrimeFactors(x):
    primeFactors = []
    for i in range(2,round(math.sqrt(x))+1):
        if x % i == 0:
            print("Found factor", i)
            if isPrime(i) == True:
                print("Found prime factor", i)
                primeFactors.append(i)
    return(primeFactors)

def isPrime(x):
    for i in range(2,round(x/2)):
        if x % i == 0:
            return False
    return True

findPrimeFactors(600851475143)