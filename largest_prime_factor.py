import sys
print(sys.version)
from array import *
import math

number = input("Enter number : ")
number = int(number)

def getFactors(n):
    factors = []
    for x in range(1, int(math.sqrt(n))):
        if n % x == 0:
            factors.append(x)
    factors = [int(x) for x in factors]
    return factors

def isPrime(num):
    isPrime = True
    for x in range(2, int(math.sqrt(num))):
        if num % x == 0:
            isPrime = False
            break;
        else:
            isPrime = True
    if isPrime:
        return True
    else:
        return False

def largest_prime_factor(number):
    lpf = 0
    factors_soreted = sorted(getFactors(number), key=int, reverse=True)
    print("Factors rversed : " + str(factors_soreted))
    for x in factors_soreted:
        if isPrime(x) and (number % x == 0):
            lpf = x
            break
    return lpf

print("Largest Prime Factor of "+ str(number) +" is :"+ str(largest_prime_factor(number)))
