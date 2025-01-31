#https://www.youtube.com/watch?v=H2U24n4bcQQ
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1

        while(j>=i):
            mid = (i+j)//2
            if nums[mid] >= nums[j]:
                i = mid+1
            else:
                j = mid      #most important line of code 
        return nums[mid]
