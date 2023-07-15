class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,sl = 0,1,0
        
        if(len(s))==1:
            return 1

        while(j<len(s)):
            if (len(s[i:j+1])==len(set(s[i:j+1]))):
                sl = max(sl,len(s[i:j+1]))
                j +=1
            else:
                i +=1
        return sl