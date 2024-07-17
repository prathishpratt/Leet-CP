class Solution:
    def isValid(self, s: str) -> bool:
        # i = 0
        # j = len(s)-1

        # while(j>i):
        #     if s[i] == "(":
        #         if s[j] != ")":
        #             return False
        #     elif s[i] == "{":
        #         if s[j] != "}":
        #             return False
        #     elif s[i] == "[":
        #         if s[j] != "]":
        #             return False
        #     i = i+1
        #     j = j-1
        # return True
        
        openclose = {']':'[', '}':'{', ')':'('}
        stack = []

        for i in range(0,len(s)):
            if s[i] in openclose.keys() and stack:
                if stack[-1] == openclose[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return False if stack else True
