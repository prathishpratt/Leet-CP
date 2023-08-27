class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Openclose = { "]" : "[", "}" : "{", ")" : "("}

        for i in s:
            if i in Openclose.keys():
                if stack and stack[-1] == Openclose[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True  