class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(20):
            n= sum([int(i)*int(i)   for i in str(n)])
            if n==1:
                return True
        return False