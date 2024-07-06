class Solution:
  #WATCH NEETCODE
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        
        has, countT = {}, {}

        for i in range(0, len(t)):
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        l = 0
        res = [-1,-1]
        reslen = float("infinity")
        have = 0
        need = len(countT)
        for r in range(0,len(s)):
            has[s[r]] = 1 + has.get(s[r],0)

            if s[r] in countT and has[s[r]] == countT[s[r]]:
                have = have + 1
            
            while(have == need):
                if r-l+1 < reslen:
                    res = [l,r]
                    reslen = r-l+1
                has[s[l]] -=1
                if s[l] in countT and has[s[l]] <countT[s[l]]:
                    have -=1
                l = l+1
        
        l, r = res[0], res[1]
        if reslen != float("infinity"):
            return s[l:r+1] 
        else:
             return ""

