import sys
print(sys.version)
import math
from datetime import datetime
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
This program intends to find the smallest positive number that is
evenly divisible (which doesn't leave any remainder) by all of the numbers from 1 to n?
'''
limit_str = input("Enter the maximum number upto which the number is evenly divisible : ")

# Start of timer
startTime = datetime.now()

limit = int(limit_str)
number_set = []
for x in range(1, limit+1):
    number_set.append(x)
number_set.sort(key=int, reverse=True)

def getPrimes(n):
    primes = [2, 3]
    for x in range(4, n+1):
        isPrime = True
        for y in range(2, x):
            if x % y == 0:
                isPrime = False
                break;
        if isPrime:
            primes.append(x)
    return primes

def getPrimeFactors(n):
    prime_factors = []
    primes = getPrimes(n)
    for prime in primes:
        while n % prime == 0:
            prime_factors.append(prime)
            n = n/prime
    return prime_factors

multipliers = []
for x in number_set:
    if(x != 1):
        multipliers.append(getPrimeFactors(x))
multipliers.sort(key=len, reverse = True)

prime_multiples ={}
for factors in multipliers:
    for prime in getPrimes(limit):
        if not(prime in prime_multiples) or (prime_multiples[prime] < factors.count(prime)):
            prime_multiples[prime] = factors.count(prime)

lowestMultiple = 1
for prime_factor in prime_multiples:
    global lowestMultiple
    lowestMultiple = lowestMultiple * (prime_factor ** prime_multiples[prime_factor])

print("Lowest multiple for first " + str(limit) + " is : " + str(lowestMultiple))
print ("Time required for execution : "+ str(datetime.now() - startTime))
