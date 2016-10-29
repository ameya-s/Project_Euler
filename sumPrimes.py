import sys
print(sys.version)
import math
import time
import pickle
import os
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
This programm intends to find the sum of all the primes below given number.
'''

limit = int(input("Enter the number upto which sum of prime numbers is required : "))
startTime = time.time()  # Start timer

# Read primes from pre-saved list
if os.path.isfile('./primes'):
    with open('primes', 'rb') as f:
        primes = pickle.load(f)
else:
    primes = []

"""
def getPrimesUptoN(n):
    global primes
    x = primes[len(primes)-1] + 1
    while primes[len(primes) - 1] < n:
        if (x+1) % 6 == 0 or (x-1) % 6 == 0 :
            isPrime = True
            for prime in primes:
                if x % prime == 0 :
                    isPrime = False
                    break
            if isPrime and x <= limit:
                primes.append(x)
        x = x + 1
    with open('primes', 'wb') as f:
        pickle.dump(primes, f)
"""

def getPrimesUptoN(n):
    global primes
    if len(primes) == 0:
        primes = [2]
    x = primes[len(primes)-1] + 1
    sieve = [True] * n
    for i in range(x,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    primes = primes + [i for i in range(x,n,2) if sieve[i]]
    with open('primes', 'wb') as f:
        pickle.dump(primes, f)

if os.path.isfile('./primes'):
    if max(primes) <= limit:
        getPrimesUptoN(limit)
else:
    getPrimesUptoN(limit)


primes = [x for x in primes if x <= limit]
print("Sum of primes till " + str(limit) + " is : " + str(sum(primes)))
print("Time Required for execution : " + str(time.time()-startTime))
