#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def get_num(s):
    open_counter = 0
    close_counter = 0
    for char in s:
        if char =="(":
            open_counter += 1

        elif char == ")":
            close_counter += 1
    return open_counter,close_counter
#O(n) time | O(1) space
def getMin(s):
    add_counter = 0
    open_counter,close_counter = get_num(s)
    loop_range = abs(open_counter-close_counter)

    for i in range(0,loop_range):
        if open_counter > close_counter:
            s += ")"
            add_counter += 1

        elif open_counter < close_counter:
            new  = "(" + s
            add_counter += 1
    return add_counter



if __name__ == '__main__':