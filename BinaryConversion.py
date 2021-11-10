#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assignment: Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in binary.

x = int(input())

while x > 0:
    print(x % 2, end='')
    x //= 2
	
print()

