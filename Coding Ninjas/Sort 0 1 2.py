#https://www.naukri.com/code360/problems/sort-0-1-2_631055?topList=love-babbar-dsa-sheet-problems&utm_source=website&utm_medium=affiliate&utm_campaign=450dsatracker&leftPanelTabValue=PROBLEM

def sort012(arr, n) :
    left = 0
    mid = 0
    right = len(arr)-1

    while(mid<=right):
        if arr[mid] == 0:
            arr[mid], arr[left] = arr[left], arr[mid]
            left +=1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid] 
            right -= 1
