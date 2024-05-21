'''https://www.naukri.com/code360/problems/reverse-the-array_1262298?topList=love-babbar-dsa-sheet-problems&utm_source=website&utm_medium=affiliate&utm_campaign=450dsatracker&leftPanelTabValue=PROBLEM'''

from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    l = len(arr)
    if m == l-1:
        return arr
    
    left = m+1
    right = l-1

    while(left<right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr 
