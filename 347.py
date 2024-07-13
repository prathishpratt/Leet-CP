class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has = {}
        
        res= []
        for i in range(0,len(nums)):
            has[nums[i]]  = 1+ has.get(nums[i],0)

        bighas = [[] for i in range(len(nums)+1)]
        for key, value in has.items():
            bighas[value].append(key)

        for i in range(len(bighas)-1,0,-1):
            for j in bighas[i]:
                res.append(j)
                if len(res) == k:
                    return res
