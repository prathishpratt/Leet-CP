#https://www.naukri.com/code360/problems/sum-of-max-and-min_1081476?topList=love-babbar-dsa-sheet-problems&utm_source=website&utm_medium=affiliate&utm_campaign=450dsatracker&leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *

def sumOfMaxMin(arr):
    # return max(arr)+min(arr)          1st method - O(2N)

    #O(N)
    mini = arr[0]
    maxi = arr[0]

    for i in arr:
        if i<mini:
            mini = i
        if i>maxi:
            maxi = i

    return mini+maxi
    
    #but apparently 1st method is better in space and time
