class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        r = 0
        prod = 1
        while(r<len(nums)): 
            prod = prod * nums[r]

            if prod>=k:
                while(l<=r and prod >= k):
                    prod = prod//nums[l]
                    l +=1
            res += (r-l+1)
            r =r+1
        return res
