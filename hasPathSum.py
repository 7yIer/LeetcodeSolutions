# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Perform a dfs
        # Sum along the path
        # Check the sum at the end
        def dfs(root, s=0):
            if root is None:
                return 
            if root.left is None and root.right is None:
                return s + root.val == targetSum
            return dfs(root.left, s + root.val) or dfs(root.right, s + root.val)
        
        return dfs(root)
