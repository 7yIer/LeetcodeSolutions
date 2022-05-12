# https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Traverse each left and right height of a root
        # Comapare these heights added to the current diameter
        
        diameter = 0
        
        def dfs(node):
            if node is None:
                return 0
            
            nonlocal diameter
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            diameter = max(diameter, left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        
        return diameter
            
