class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        lst = []
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break
            
            j = i+1
            k = len(nums)-1

            while(j<k):
                tot = nums[i] + nums[j] + nums[k]

                if tot < 0:
                    j = j +1
                elif tot > 0:
                    k = k -1
                else:
                    if [nums[i], nums[j], nums[k]] not in lst:
                        lst.append([nums[i], nums[j], nums[k]])
                    j = j+1
                    k = k-1
        return lst
