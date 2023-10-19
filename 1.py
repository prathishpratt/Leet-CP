class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}

        for items in range(0,len(nums)):
            if target-nums[items] in has.keys():
                return items, has[target-nums[items]]
            else:
                has[nums[items]] = items