# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 

        res = 0

        #calculates the diameter but returns height
        def dfs(root):
            if root == None:
                return 0
            
            nonlocal res    #meaning its the global
            #that the local function is accessing the global variable

            left = dfs(root.left)
            right = dfs(root.right)
            diameter = left + right

            res = max(res,diameter)
            return 1 + max(left,right)
        
        dfs(root)
        return res
