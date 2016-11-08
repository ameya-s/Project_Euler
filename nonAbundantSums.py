import sys
print(sys.version)
import math
import time
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

abundants = []
def isAbundant(n):
    sum = 1
    if n % 2 == 0 :
        step = 2
        sum = sum + 2
    else:
        step = 1
    for x in range(3, int(math.sqrt(n))+1, step):
        if n % x == 0:
            sum = sum + x + n/x

    return sum > n

non_abundant_sum = 0

for x in range(12, 28124):
    if isAbundant(x):
        abundants.append(x)
print(len(abundants))

for x in range(1, 28124):
    unit_sum = 0
    for i in range(12, x):
        if i in abundants and (x-i) in abundants:
            unit_sum = 0
            break;
        unit_sum = x
    non_abundant_sum = non_abundant_sum + unit_sum



print("Non abundant sum is : " + str(non_abundant_sum))
print("Time Required for execution : " + str(time.time()-startTime))
