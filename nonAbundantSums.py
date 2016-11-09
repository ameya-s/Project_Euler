import sys
print(sys.version)
import math
import time
import itertools
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the
sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though
it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
startTime = time.time() # Start timer
limit = 28123  #According to Wolfram Mathworld’s discussion on Abundant Numbers, “Every number greater than 20161 can be expressed as a sum of two abundant numbers. ” So our upper bound is 20161 instead of 28123.
abundants = set()

def sumFactors(n):
    sumF = 1
    t = n**0.5
    for x in range(2, int(t+1)):
        if n % x == 0:
            sumF += x + n/x
    if t == int(t): sumF -= t    #correct s if t is a perfect square
    return sumF

non_abundant_sum = 0

for x in range(1, limit+1):
    if sumFactors(x) > x :
        abundants.add(x)
    if not any((x-a in abundants) for a in abundants):
        non_abundant_sum += x

print("Non abundant sum is : " + str(non_abundant_sum))
print("Time Required for execution : " + str(time.time()-startTime))
