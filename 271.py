class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in strs:
            for j in i:
                j = chr(ord(j)+1)            #Shift the letter by 1 using ascii 
        return strs

    def decode(self, s: str) -> List[str]:
        for i in s:
            for j in i:
                j = chr(ord(j)-1)            #Shift the letter by 1 back using ascii 
        return s
