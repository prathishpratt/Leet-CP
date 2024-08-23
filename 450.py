# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def findmin(root):
            while root and root.left:
                root = root.left
            return root

        if not root:
            return None
        if val < root.val:
            root.left = self.deleteNode(root.left,val)
        elif val > root.val:
            root.right = self.deleteNode(root.right,val)
        
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                mini = findmin(root.right)
                root.val = mini.val
                root.right = self.deleteNode(root.right,mini.val)
        return root
        
