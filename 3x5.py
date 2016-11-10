#! python
import sys
print(sys.version)

limit = input("Enter limit : ")
limit = int(limit)
sum = 0;

def getMultiples(limit):
    global sum
    if limit > 3 and limit > 5:
        # Block of Function
        for x in range(limit):
            if( x % 3 == 0 or x % 5 == 0):
                sum = sum + x
    else:
        return "Enter a valid number"

    return sum

print("Output: " + str(getMultiples(limit)))
