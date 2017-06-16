# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:59:16 2017

@author: Steven
"""

import math
import timeit
start = timeit.default_timer()

def is_perfect_square(n):
	if float(n).is_integer():
		return True
	else:
		return False

for a in range(2,500):
	for b in range(a+1,500):
		c = a**2 + b**2
		if is_perfect_square(c):
			sum = a + b + math.sqrt(c)
			if sum == 1000:
				print ("%d + %d + %d = 1000" % (a,b,math.sqrt(c)))
				print(a*b*math.sqrt(c))
				
stop = timeit.default_timer()
print (stop - start,"seconds")