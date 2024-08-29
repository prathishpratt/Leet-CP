class Solution:   
    def isSubtree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root2:
            return True
        if root1 == None:
            return False

            
        def isSameTree(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False

            return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        if root1.val == root2.val:
            flag = isSameTree(root1, root2)
        else:
            flag = False
        return  flag or self.isSubtree(root1.left, root2) or self.isSubtree(root1.right, root2)
