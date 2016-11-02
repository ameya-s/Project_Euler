import sys
print(sys.version)
import math
import time

startTime = time.time() # Start timer

txt = open('100_50digit_Numbers.txt')
numbers = txt.read()
numbers = numbers.split("\n")
numbers = [int(x) for x in numbers if x is not ""]

sum  = 0
for number in numbers:
    sum = sum + number

sum_str = str(sum)

print("First ten digits of sum are : "+ sum_str[0:10])
print("Time Required for execution : " + str(time.time()-startTime))
