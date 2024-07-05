class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        hass = {}
        has = {}
        l = 0
        r = len(s1)-1 
        for i in range(0, len(s1)):
            has[s1[i]] = 1 + has.get(s1[i],0)
        for i in range(0, len(s1)-1):
            hass[s2[i]] = 1 + hass.get(s2[i],0)

        while(r<len(s2)):
            hass[s2[r]] = 1 + hass.get(s2[r],0)

            if hass == has:
                return True
            if hass[s2[l]] == 1:
                del hass[s2[l]]
            else:
                hass[s2[l]] -= 1
            l = l+1
            r = r+1
        return False

#SLOW SOLUTION
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:

#         l = 0
#         r = len(s1)-1

#         while(r<len(s2)):
#             if set(s1) == set(s2[l:r+1]):
#                 if sorted(s1) == sorted(s2[l:r+1]):
#                     return True
#             l +=1
#             r +=1 
#         return False
