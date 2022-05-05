# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Put every number in nums into a dictionary
        # Loop for 0 to n checking that the number is in the dictionary
        # Return the value that is not in the dictionary
        
        d = {}
        
        for num in nums:
            d[num] = True
                
        for i in range(len(nums) + 1):
            if i in d:
                continue
            else:
                return i
        
