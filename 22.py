class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        def backtrack(para, openn, close, n):
            if openn == close == n:
                lst.append(para)
                return
            if openn < n:
                backtrack(para+"(", openn +1, close, n)
            if close < openn:
                backtrack(para+")", openn, close +1, n)
            
        backtrack("", 0, 0, n)
        return lst
