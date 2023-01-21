# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Perform a DFS 
        # Keep returning the bottom level and getting the minimum of that
        if not root:
            return 0
        
        def dfs(root, level=1):
            if root is None:
                return math.inf
            if not root.left and not root.right:
                return level
            return min(dfs(root.left, level + 1), dfs(root.right, level + 1))

        return dfs(root)
