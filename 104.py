# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))

        # lst = []

        # def traverse(root, val, lst):
        #     if root == None:
        #         return
        #     val = val +1
        #     if root.left == None and root.right == None:
        #         lst.append(val)
        #         return

        #     traverse(root.left, val, lst)
        #     traverse(root.right, val, lst)

        # traverse(root, 0 ,lst)
        # return max(lst) if lst else 0
