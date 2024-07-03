class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = max(piles)
        while(l<=r):
            mid = (l+r)//2
            res = 0
            for j in piles:
                res += math.ceil(j / mid)
            if res<=h:
                k = mid
                r=mid-1
            else:
                l = mid+1
        return k
