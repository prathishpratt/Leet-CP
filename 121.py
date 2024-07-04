class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        i, j = 0, 0 

        if len(prices)<2:
            return 0
        
        while(j<len(prices)):
            if (prices[j]>= prices[i]):
                prof = max(prices[j]-prices[i], prof)
            else:
                i = j
            j=j+1
        return prof
