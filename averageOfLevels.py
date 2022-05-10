# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Perform a regular BFS and sum on the levels.
        ans = []
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            s = 0
            for i in range(qLen):
                node = q.popleft()
                if node:
                    s += node.val
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            avg = s / qLen
            ans.append(avg)
        return ans
        # Create a dictionary
        # Traverse the tree storing each level as a key and appending the values to an arr
        # Loop the dictionary keys and compute the average from the array
        d = {}
        ans = []
        def dfs(root, level=1):
            if root is None:
                return
            
            if level in d:
                d[level].append(root.val)
            else:
                d[level] = [root.val]
            
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        
        dfs(root)
        
        keys = d.keys()
        
        for key in keys:
            avg = sum(list(d[key])) / len(list(d[key]))
            ans.append(avg)
        
        return ans
        
