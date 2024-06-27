class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        p_ = len(p)
        s_hash = {}
        p_hash = {}
        lst = []

        for i in range(0,len(p)):
            s_hash[s[i]] = 1 + s_hash.get(s[i],0)
            p_hash[p[i]] = 1 + p_hash.get(p[i],0) 
        
        if s_hash == p_hash:
            lst.append(0)

        for i in range(1,len(s)-p_+1):
            s_ = i + p_ - 1
            s_hash[s[i-1]] -= 1
            if s_hash[s[i-1]] == 0:
                del s_hash[s[i-1]]

            s_hash[s[s_]] = 1 + s_hash.get(s[s_],0)
            if s_hash == p_hash:
                lst.append(i)
        
        return lst
