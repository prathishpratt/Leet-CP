class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,summ,r=0,0,1
        if len(prices)==1:
            return 0
        
        while(r<len(prices)):
            if prices[l]<=prices[r]:
                summ = max(summ,prices[r]-prices[l])
                r = r+1
            else:
                l = r
                r= r+1
        return summ