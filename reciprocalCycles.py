#! python
import sys
print(sys.version)
import math
import time
from collections import defaultdict

'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

limit = int(input("Enter the limit : "))
startTime = time.time() # Start timer

quotient_str_array = []
for n in range(1, limit+1):
    quotient = 1/n
    quotient_str = str(quotient).replace("0.", "")
    quotient_str_array.append(quotient_str)

recurring_unit = ""
assoc_num = None
for quotient_str in quotient_str_array:
    for i in range(len(quotient_str)):
        foundNextIndex = True
        index = i
        startDigit = quotient_str[0]
        while foundNextIndex:
             try:
                 temp_index = quotient_str.index(startDigit, index+1)
                 recurring_unit_temp = quotient_str[index:temp_index]
                 if recurring_unit_temp == quotient_str[index + len(recurring_unit_temp):temp_index + len(recurring_unit_temp)] and len(recurring_unit) < len(recurring_unit_temp):
                     recurring_unit = recurring_unit_temp
                     assoc_num = 1/float("0." + quotient_str)
                 index = temp_index
             except ValueError:
                 foundNextIndex = False

print(recurring_unit)
print(assoc_num)
print("Time Required for execution : " + str(time.time()-startTime))
