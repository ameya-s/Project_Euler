#! python
import sys
print(sys.version)
import math
import time
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''
number = int(input("Enter the number : "))
power = int(input("Enter the exponent : "))
startTime = time.time()

powerDigits = list(str( number ** power))
sum = 0

for digit in powerDigits:
    sum = sum + int(digit)

print("Sum of power digits is : " + str(sum))
print("Time Required for execution : " + str(time.time()-startTime))
