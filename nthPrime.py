import sys
print(sys.version)
import math
import time
import pickle
'''
This program intends to find the nth prime number.
'''

nth = int(input("Enter the numeric position at which prime number is required : "))
startTime = time.time() # Start timer

primes = None

# Read pre saved primes and load into a list
with open('primes', 'rb') as f:
    primes = pickle.load(f)

# Function to generate first n primes
def getPrimes(n):
    global primes
    x = primes[len(primes)-1]+1
    while len(primes) < n:
        isPrime = True
        for prime in primes:
            if x % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(x)
        x = x + 1
    with open('primes', 'wb') as f:
        pickle.dump(primes, f)

# Check if pre saved file has required first n primes. If not then generate new primes with the function above
if(len(primes) < nth):
    getPrimes(nth)

print(str(nth) + "th prime : " + str(primes[nth-1]))
print("Time Required for execution : " + str(time.time()-startTime))
