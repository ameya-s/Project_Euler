import sys
print(sys.version)
from array import *

limit = 4000000

def getFiboSum_even(limit):
    t1 = 1
    t2 = 2
    next = 0
    sum = t2
    print("Getting sum...")
    while(next < limit):
        next = t1+t2
        if next % 2 == 0:
            sum = sum + next
        t1 = t2
        t2 = next
    print("Finished loop...")

    return sum

print("Sum of even Fibonacci terms till "+str(limit)+" is : "+ str(getFiboSum_even(limit)))
