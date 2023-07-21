class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        lst =[]

        for i in range(0,n-2):
            if nums[i] == nums[i-1] and i>0:
                continue
            
            j = i+1
            k = n-1

            while(j<k):
                summ = nums[i]+nums[j]+nums[k]
                if summ == 0:
                    if [nums[i],nums[j],nums[k]] not in lst:
                        lst.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                elif(nums[i]+nums[j]+nums[k]<0):
                    j +=1
                else:
                    k -=1

        return lst 
       