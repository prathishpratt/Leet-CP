class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 0

        sets = set(nums)
        #check if right does not exist
        for i in nums:
            leng = 1
            if i + 1 not in sets:
                while i-1 in sets:
                    leng += 1
                    i -= 1
                maxi = max(maxi,leng)

        return maxi     
        #     if i-1 not in sets:
        #         while (i+1) in sets:
        #             leng +=1
        #             i = i+1
        #         maxi = max(leng,maxi)
        # return maxi 


        #check if left does not exist 
        
        # seen = set(nums)
        # longest = 0
        # for n in seen:
        #     if (n-1) not in seen:
        #         length = 1
        #         while(n+length) in seen:
        #             length +=1
        #         longest = max(longest, length)
        # return longest
