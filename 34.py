class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binsearch(nums, target, flag = 1)
        right =  self.binsearch(nums, target, flag = 0)
        return [left,right]

    def binsearch(self, nums, target, flag):
        l = 0
        r = len(nums) -1
        i = -1
        while(l<=r):
            m = (l + r)//2
            
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                if flag:
                    i = m
                    r=m-1
                else:
                    i = m
                    l =m+1
        return i
