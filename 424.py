class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        has = {}
        res=0

        while(r<len(s)):
            has[s[r]] = 1+ has.get(s[r],0)
            if (r-l+1)-max(has.values()) >k:
                has[s[l]] -= 1
                l +=1
            res = max(res,r-l+1)
            r +=1
        return res
