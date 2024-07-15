class Solution:
    def trap(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l ,r =0, len(nums)-1
        leftmax = nums[l]
        rightmax = nums[r]
        res = 0

        while(l<r):
            if leftmax<=rightmax:
                l +=1
                leftmax = max(leftmax,nums[l])
                res= res + leftmax - nums[l]
            else:
                r =r-1
                rightmax = max(rightmax,nums[r])
                res= res + rightmax - nums[r]
        return res
