class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Neetcode's first solution
      
        k = len(nums)+1
        front = [1]*(len(nums)+1)
        rear = [1]*(len(nums)+1)
        ans = [1]*(len(nums))

        for i in range(1,k):
            front[i] = front[i-1]*nums[i-1]
        for i in range(len(nums), 0, -1):
            rear[i-1] = rear[i]*nums[i-1]
        for i in range(0, len(nums)):
            ans[i] = front[i]*rear[i+1]
        return ans
