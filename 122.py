class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        addi = 0
        n = len(prices)
        if n<2:
            return 0
        
        while(j<n):
            if(prices[j]<prices[i]):
                i = j
                j +=1
            else:
                k = j
                try:
                    while(prices[k]<=prices[k+1]):
                        k = k+1
                except:
                    pass      
                j = k+1
                addi += (prices[k]-prices[i])
                i = k
        return addi
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit=0
#         for i in range(1,len(prices)):
#             if prices[i]>prices[i-1]:
#                 profit+=prices[i]-prices[i-1]
#         return profit