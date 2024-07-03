class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      #First do a binary search of which row has the range of the target and then do another binary search to get the target itself. 
        lengt, lengd = len(matrix), len(matrix[0])
        d = lengt-1
        t = 0
        flag = -1

        while(t<=d):
            mid = (t+d)//2
            if matrix[mid][-1] < target:
                t = mid+1
            elif matrix[mid][0] > target: 
                d = mid-1
            else:
                flag = mid
                break
        if flag == -1:
            return False
        l = 0
        r = len(matrix[flag])-1
        while(l <= r):
            m = (l+r)//2
            if matrix[flag][m] < target:
                l = m+1
            elif matrix[mid][m] > target:
                r = m-1
            else:
                return True
        return False
                    
        
