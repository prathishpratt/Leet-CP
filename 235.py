# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val >= min(p.val, q.val) and root.val <= max(p.val,q.val):
            return root
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
            
        # lst1, lst2 = [], []
        # def find(root, target, lst):
        #     if root == None:
        #         return None
        #     lst.append(root.val)
        #     if target < root.val:
        #         return find(root.left,target, lst)
        #     elif target == root.val:
        #         return lst
        #     else:
        #         return find(root.right, target,lst)

        # lst1 = find(root, p.val, lst1)
        # lst2 = find(root, q.val, lst2)
        
        # for i in range(len(lst1)-1, -1,-1):
        #     if lst1[i] in lst2:
        #         return TreeNode(lst1[i])
