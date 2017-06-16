# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 04:36:43 2017

@author: Steven
"""

with open('euler-013.txt') as f:
    lines = [line.rstrip('\n') for line in open('euler-013.txt')]

sum = 0
for i in range(0,len(lines)):
    sum += int(lines[i][0:12])
    
print(str(sum)[0:10])