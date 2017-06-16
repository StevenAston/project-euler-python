# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 03:41:36 2017

@author: Steven
"""

import timeit
start = timeit.default_timer()

def sum_of_squares(n):
	sum = 0
	for i in range(1, n+1):
		sum += i**2
	return sum

def square_of_sum(n):
	sum = 0
	for i in range(1, n+1):
		sum += i
	return sum**2

def difference(n):
	return (square_of_sum(n) - sum_of_squares(n))

print (difference(100))

stop = timeit.default_timer()
print (stop - start,"seconds")