def separateNegativeAndPositive(nums):  
    l, h = 0, len(nums)-1

    while(h>l):
        if (nums[l]>0):
            if(nums[h]<0):
                nums[l], nums[h] = nums[h], nums[l]
                l += 1
                h -= 1
            else:
                h -= 1
        else:
            l += 1

    return nums
