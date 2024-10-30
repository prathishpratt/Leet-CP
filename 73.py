class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        colums = set()

        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    colums.add(j)

    #set rows = 0
        for i in rows:
            for j in range(0,len(matrix[0])):
                matrix[i][j] = 0

    #set cols = 0
        for i in range(0,len(matrix)):
            for j in colums:
                matrix[i][j] = 0

        return matrix
