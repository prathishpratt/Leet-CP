class Solution:
    def carFleet(self, target: int, nums: List[int], speed: List[int]) -> int:
        stack = []
        pair = []

        for i in range(0,len(nums)):
            pair.append([nums[i],speed[i]])

        pair = sorted(pair)

        for i in range(len(pair)-1,-1,-1):
            res = (target - pair[i][0]) / pair[i][1]

            if stack:
                if stack[-1] < res:
                    stack.append(res)
            else:
                stack.append(res)

        return len(stack)
        
