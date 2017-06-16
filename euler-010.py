# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:59:16 2017

@author: Steven
"""

import timeit
from primesieve import generate_primes
start = timeit.default_timer()

print(sum(generate_primes(2000000)))

stop = timeit.default_timer()
print (stop - start,"seconds")