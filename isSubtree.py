class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        def isSameTree(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None or root2 is None:
                return False
            else:
                return root1.val == root2.val and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        def searchForSubTree(head, sub):
            if head is None:
                return False
            if isSameTree(head, sub):
                return True
            return searchForSubTree(head.left, sub) or searchForSubTree(head.right, sub)
        
        return searchForSubTree(root, subRoot)
