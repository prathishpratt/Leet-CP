class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Try to write the logic by your own, I did it with trial and error
        l, r = 0, len(nums)-1
        k = 10000
        while(l<=r):
            mid = (l+r)//2
            k = min(k,nums[mid])
            if nums[mid]>=nums[l] and nums[mid]>=nums[r]:
                l = mid +1
            else:
                r = mid -1
        return k
