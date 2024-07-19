class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res=[0 for i in range(0,len(nums))]
        stack = [] #store as a tuple of (value, index)

        for i in range(0,len(nums)):
            while stack and stack[-1][0] < nums[i]:
                k = stack.pop()
                res[k[1]] = i - k[1]
            stack.append((nums[i],i))
        return res


# class Solution:
#     def dailyTemperatures(self, nums: List[int]) -> List[int]:
#         res=[]
#         for i in range(0,len(nums)):
#             count = 0
#             flag = 0
#             for j in range(i+1,len(nums)):
#                 count = count+1
#                 if nums[j]>nums[i]:
#                     flag = 1
#                     break
#             if count != 0 and flag == 1:
#                 res.append(count)
#             else:
#                 res.append(0)
#         return res
        
