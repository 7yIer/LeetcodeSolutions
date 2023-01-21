# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        leaveSum = {}
        def dfs(root, depth=0):
            if root is None:
                return
            if root.left is None and root.right is None:
                if depth in leaveSum:
                    leaveSum[depth] = leaveSum[depth] + root.val
                else:
                    leaveSum[depth] = root.val
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            
        dfs(root)    
        
        keys = leaveSum.keys()
        maxDepth = max(keys)
        
        return leaveSum[maxDepth]
