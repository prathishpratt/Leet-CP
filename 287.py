class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow

        #With extra space
        # dicti = {}

        # for i in range(0, len(nums)):
        #     if nums[i] in dicti.keys():
        #         return nums[i]
        #     else:
        #         dicti[nums[i]] = i
