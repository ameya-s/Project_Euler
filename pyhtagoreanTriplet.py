import sys
print(sys.version)
import math
import time
import pickle
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
sumTriplet = int(input("Enter sum of Pythagorean triplet : "))
startTime = time.time() # Start timer

productTriplet = None
triplet = []

'''
Using Euclid's formula for finding Pythgorean triplets
a = m^2 - n^2
b = 2*m*n
c = m^2 + n^2
where m > n >0 and a^2 + b^2 = c^2
'''

def getFactors(n):
    factors = []
    for x in range(1, int(math.sqrt(n))):
        if n % x == 0 :
            factors.append(x)
            factors.append(n/x)
    factors.sort()
    return factors

for m in getFactors(sumTriplet/2):
    n = (sumTriplet/(2*m))- m
    if m > n:
        a = m ** 2 - n ** 2
        b = 2*m*n
        c = m ** 2 + n ** 2

        if a + b + c == sumTriplet :
            productTriplet = a * b * c
            triplet.append([a,b,c])
            break

print("Product of triplet whose sum is 1000 : " + str(productTriplet))
print("Time Required for execution : " + str(time.time()-startTime)) # First method  =  25.00349998474121
