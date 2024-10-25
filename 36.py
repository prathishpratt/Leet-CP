class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.':
                    res += [(i,board[i][j]), (board[i][j], j), (i//3,j//3, board[i][j])]
        return len(res) == len(set(res))

#Bad Solution
# for i in range(9):
#             for j in range(9):
#                 x = board[i][j]
#                 if x!= '.':
#                     y = [(i,x), (x, j), (i//3,j//3, x)]
#                     for j in y:
#                         if j in res:
#                             return False
#                         else:
#                             res.append(j)
#         return True


#Another solution

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         board = np.array(board)

#         for i in range(0,9):
#             lst = []
#             for j in range(0,9):
#                 if board[i][j] in lst and board[i][j] != ".":
#                     return False
#                 else:
#                     lst.append(board[i][j])
            
#         for i in range(0,9):
#             lst = []
#             for j in range(0,9):
#                 if board[j][i] in lst and board[j][i] != ".":
#                     return False
#                 else:
#                     lst.append(board[j][i])

#         for i in range(0,9,3):
#             for j in range(0,9,3):
#                 cst = board[i:i+3, j:j+3]
#                 lst = []
#                 for k in range(0,3):
#                     for l in range(0,3):
#                         if cst[k][l] in lst and cst[k][l] != ".":
#                             return False
#                         else:
#                             lst.append(cst[k][l])
        
#         return True
