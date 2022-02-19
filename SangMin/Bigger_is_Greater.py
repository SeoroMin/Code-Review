#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    
    w_list = list(w)
    
    swap = False
    for i in range(len(w_list)-1, 0, -1):
        if w_list[i] > w_list[i-1]:
            w_list[i], w_list[i-1] = w_list[i-1], w_list[i]
            swap = True
            break
    
    if (swap == False):
        return "no answer"
    
    return w_list
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)
        
        print(result)

        #fptr.write(result + '\n')

    #fptr.close()
