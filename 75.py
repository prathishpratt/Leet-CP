class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        l = 0
        m = 0
        h = len(nums)-1

        while(m<=h):
            if nums[m] == 0:
                nums[m],nums[l] = nums[l], nums[m]
                m = m+1
                l = l+1
            elif nums[m] == 1:
                m = m+1
            elif nums[m] == 2:
                nums[m],nums[h] = nums[h], nums[m]
                h = h-1