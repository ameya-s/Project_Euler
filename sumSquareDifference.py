import sys
print(sys.version)
import math
from datetime import datetime

'''
The sum of the squares of the first ten natural numbers is,1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between above two is 3025 − 385 = 2640.
This program intends to find the difference between
the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

limit = int(input("Enter the number upto which difference between sum of squares and square of sums is required: "))
# Start of timer
startTime = datetime.now()

def sumOfSquares(n):
    sum = 0
    for x in range(n+1):
        sum = sum + x ** 2
    return sum

def squareOfSum(n):
    sum = 0
    for x in range(n+1):
        sum = sum + x
    return (sum ** 2)

print("Difference is : "+ str(squareOfSum(limit)-sumOfSquares(limit)))
