class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Using flyod's algorithm
        slow,fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast:
                return slow

        #With extra space
        # dicti = {}

        # for i in range(0, len(nums)):
        #     if nums[i] in dicti.keys():
        #         return nums[i]
        #     else:
        #         dicti[nums[i]] = i