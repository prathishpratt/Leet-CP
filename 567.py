class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        r = len(s1)-1

        while(r<len(s2)):
            if set(s1) == set(s2[l:r+1]):
                if sorted(s1) == sorted(s2[l:r+1]):
                    return True
            l +=1
            r +=1 
        return False