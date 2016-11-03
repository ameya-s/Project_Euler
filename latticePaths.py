import sys
print(sys.version)
import math
import time
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''
grid_size = int(input("enter the size of square grid : "))+1
startTime = time.time() # Start timer
grid = [[1 for x in range(grid_size)] for y in range(grid_size)]

for y in range(1,len(grid)):
        for x in range(1,len(grid[y])):
            grid[y][x] = grid[y-1][x] + grid[y][x-1]

print(grid[len(grid)-1][len(grid[len(grid)-1])-1])
print(grid)
print("Time Required for execution : " + str(time.time()-startTime))
