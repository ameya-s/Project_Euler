#! python
import sys
print(sys.version)
import math
import time
'''
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
This program intends to find the greatest product of thirteen adjacent digits in the 1000-digit number.
'''
digitGroupLength = int(input("Enter the length of series : "))
startTime = time.time() # Start timer

f = open('thousandOaks.txt', 'r')
thousandOaks = f.read()
splitOaks = list(thousandOaks)
finalProduct = 1
finalDigitGroup = []
for x in range(len(splitOaks)-digitGroupLength):
    digitGroup = splitOaks[x:(x+digitGroupLength):1]
    product = 1
    for digit in digitGroup:
        product = product * int(digit)
        if product > finalProduct:
            finalProduct = product
            finalDigitGroup = digitGroup

print("Largest product is : "+ str(finalProduct))
print("Adjacent digits are : " + str(finalDigitGroup))
print("Time Required for execution : " + str(time.time()-startTime))
