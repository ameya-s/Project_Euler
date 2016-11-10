#! python
import sys
print(sys.version)
import math
import time
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
startTime = time.time() # Start timer

a = 1
b = 1
next_fibo = 0
index = 2
while len(str(next_fibo)) < 1000 :
    next_fibo = a + b
    a = b
    b = next_fibo
    index = index + 1


print("Index of required fibonacci number : " + str(index))
print("Time Required for execution : " + str(time.time()-startTime))
