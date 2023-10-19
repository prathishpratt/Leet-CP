class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sh = {}
            th = {}
            for items in s:
                sh[items] = sh.get(items,0)+1 
            for items in t:
                th[items] = th.get(items,0)+1
            return sh == th
        return False