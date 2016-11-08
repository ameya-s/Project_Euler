import sys
print(sys.version)
import math
import time
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
'''
limit = int(input("Enter the number till which pairs are required : "))
startTime = time.time() # Start timer

def sumFactors(n):
    factors = []
    for x in range(1, int(math.sqrt(n))+1):
        if n % x == 0:
            factors.append(x)
            if n/x != n :
                factors.append(n/x)

    return sum(factors)

amicable_pairs = []
for x in range(1, limit+1):
    sum_x = sumFactors(x)
    sum_y = sumFactors(sum_x)
    if int(sum_y) == int(x) and x != sum_x and x not in amicable_pairs and sum_x not in amicable_pairs:
          amicable_pairs.append(x)
          amicable_pairs.append(sum_x)
          
print("Sum of amicable pairs is  : " + str(sum(amicable_pairs)))
print("Time Required for execution : " + str(time.time()-startTime))
