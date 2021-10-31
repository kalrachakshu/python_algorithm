#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    def get_mean(arr):
        sum_1 = sum(arr)
        n = len(arr)
        return sum_1 / n

    mean = get_mean(arr)
    mean_sq_diff_sum = sum([(x - mean) ** 2 for x in arr])
    std_dev = (mean_sq_diff_sum / len(arr)) ** 0.5
    print(round(std_dev, 1))


if __name__ == '__main__':
    # n = int(input().strip())

    vals = [10, 40, 30, 50, 20]

    stdDev(vals)
