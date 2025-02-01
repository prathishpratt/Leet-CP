class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = { ")" : "(", "]" : "[", "}" : "{" }
        
        for i in range(0,len(s)):
            if s[i] in valid.keys():
                if stack and stack[-1] == valid[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if stack:
            return False
        else:
            return True
