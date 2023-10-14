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
    
    #if you need the substring itself then,
    # def longest_substring(s):
    # """
    # input: string
    # output: longest substring without repeating characters
    # """
    # i = 0
    # j = 1
    # leng = ""
    # while(j < len(s)):
    #     t = s[i:j]

    #     if len(t) == len(set(t)):
    #         j = j+1
    #     else:
    #         t = t[0:-1]
    #         if len(t)>len(leng):
    #             leng = t
    #         i = i+1
    #         j = j+1
    # return leng