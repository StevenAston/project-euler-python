# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 04:20:52 2017

@author: Steven
"""
from factors import factors

def generate_nth_triangle(n):
    number = 0
    for i in range(1,n+1):
        number += i
    return(number)
    
max_factors = 1
n = 0

while max_factors < 500:
    n+=1
    i = generate_nth_triangle(n)
    if len(factors(i)) > max_factors:
        max_factors = len(factors(i))
        print(i, " - ", max_factors) 