#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def boom(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    column_len = len(grid[0])
    
    for i in range(len(grid)):
        print(i)
        for j in range(column_len):
            if (grid[i][j] == 'O'):
                for m in range(4):
                    nx = i + dx[m]
                    ny = j + dy[m]
                    print("grid:",grid[nx][ny])
                    grid[nx][ny] = '.'
    
    return boom(grid)

def bomberMan(n, grid):
    # Write your code here    
    
    
    column_len = len(grid[0])
    
    if n % 3 == 1:
        if n == 1:
            return grid
        else:
            n = n-3
            boom(grid)
                
    if n % 3 == 2:
        for i in range(len(grid)):
            for j in range(column_len):
                grid[i][j] == 'O'
    
    if n % 3 == 0:
        # 여기 탈출조건 어떻게 만들지..
        if n == 3:
            boom(grid)
        else:
            n = n-3
            boom(grid)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    print(result)

    #fptr.write('\n'.join(result))
    #fptr.write('\n')

    #fptr.close()