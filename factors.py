# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 04:28:55 2017

@author: Steven
"""
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))