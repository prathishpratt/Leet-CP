#See this video: https://www.youtube.com/watch?v=ZGMw8Bvpwd4
class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        res = max(nums)
        stack = []
        r = 0

        while(r<len(nums)):
            start = r
            while(stack and stack[-1][0]>nums[r]):
                h,w = stack.pop()
                res = max(res, h*(r-w))
                start = w
            stack.append((nums[r], start))
            r = r+1

        while stack:
            h, w = stack.pop()
            res = max(res, h*(len(nums)-w))

        return res

        # res = max(heights)

        # for i in range(0,len(heights)-1):
        #     mini = heights[i]
        #     for j in range(i+1, len(heights)):
        #         mini = min(mini, heights[j])
        #         res = max(res, mini*(j-i+1))

        # return res
