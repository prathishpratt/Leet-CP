class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumi = 0
        ans_sum = max(nums)

        for i in range(0,len(nums)):
            if (sumi + nums[i] < 0):
                sumi = 0
            else:
                sumi += nums[i]
                ans_sum = max(ans_sum, sumi)
        return ans_sum
