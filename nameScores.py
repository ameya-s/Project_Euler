#! python
import sys
print(sys.version)
import math
import time
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
'''
startTime = time.time() # Start timer
alphabetical_positions = {'a':1,'b':2,'c':3,}

f = open('p022_names.txt', 'r')
names = f.read().split(",")
names = [x.replace('"','') for x in names]
names = [x.replace('\n','') for x in names]
names.sort()
names_score = 0
for i in range(len(names)):
    score = sum([ord(char) - 96 for char in names[i].lower()]) * (i+1)
    names_score = names_score + score

print("Names score is : "+ str(names_score))
print("Time Required for execution : " + str(time.time()-startTime))
