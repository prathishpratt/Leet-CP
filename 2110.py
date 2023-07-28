class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ret = len(prices)
        k=0
        if ret<2:
            return ret
        i=1
        while(i<len(prices)):
            if (prices[i] == (prices[i-1]-1)):
                k = k+1
                ret +=k
            else:
                k=0
            i = i+1
        return ret