class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []

        for i in queries:
            k = 0
            for j in points:
                dist = ((j[0]-i[0])**2 + (j[1]-i[1])**2)**0.5

                if dist<=i[2]:
                    k +=1
            res.append(k)
        return res    
