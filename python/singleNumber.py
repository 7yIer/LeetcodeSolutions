# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Create a dictionary of num: count
        # Loop over the keys of the dictionary
            # Find the key with count of 1
          
        d = {}
        
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            
        keys = d.keys()
        
        for key in keys:
            if d[key] == 1:
                return key
