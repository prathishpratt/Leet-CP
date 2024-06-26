class Solution:
    def isPalindrome(self, s: str) -> bool:
        #EXTRA MEMORY
        # k = []
        # for i in s:
        #     if i.isalnum():
        #         k = k+[i.lower()]
        # return k == k[::-1]
        
        l = 0
        r = len(s)-1

        #2 POINTER
        while(r>=l):
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            elif s[l].isalnum():
                r -=1
            else:
                l +=1
        return True
