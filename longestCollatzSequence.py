import sys
print(sys.version)
import math
import time
import operator
'''
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
'''
startTime = time.time() # Start timer

chain_start = 1000000
chains = {}
for x in range(chain_start, 1, -1):
    next  = x
    count = 0
    proceed = True
    chains[x] = []
    if len(chains) > 0:
        for z in chains:
            if next in chains[z]:
                print("found match")
                chains[next] = chains[z]
                proceed = False
                break
    chains[x] = [next]
    while next > 1 and proceed:
        if next % 2 == 0 :
            next = next / 2
        else:
            next = 3*next + 1
        chains[x].append(next)
        count = count + 1

    print(chains)

print("Result : "+ str(len(chains['837799']))) #str(result))
print("Time Required for execution : " + str(time.time()-startTime))
