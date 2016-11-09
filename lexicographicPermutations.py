import sys
print(sys.version)
import math
import time
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
startTime = time.time() # Start timer

given_string = '0123456789'

def permutations(word):
    if len(word)<=1:
        return [word]

    #get all permutations of length N-1
    perms = permutations(word[1:])
    char = word[0]
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

permutationsOfGivenString = permutations(given_string)
permutationsOfGivenString.sort()

print(permutationsOfGivenString[1000000-1])
print("Time Required for execution : " + str(time.time()-startTime))
