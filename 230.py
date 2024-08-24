# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []

        def traverse(root,lst):
            if not root:
                return

            traverse(root.left,lst)
            lst.append(root.val)
            traverse(root.right,lst)

        traverse(root,lst)

        return lst[k-1]
