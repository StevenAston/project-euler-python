# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:59:16 2017

@author: Steven
"""

import timeit
start = timeit.default_timer()

def isPrime(x):
    for i in range(2,round(x/2)):
        if x % i == 0:
            return False
    return True

def find_nth_prime(n):
	prime = 1
	counter = 2
	while prime <= n:
		counter += 1
		if isPrime(counter):
			prime += 1
			if prime % 500 == 0:
				print("#",prime,counter)
	return(counter)

print(find_nth_prime(10001))

stop = timeit.default_timer()
print (stop - start,"seconds")