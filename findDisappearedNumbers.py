# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Put all of the values into a dictionary.
        # Loop from 1 to n + 1
        # Put any value that is missing into an array.
        
        d = {}
        ans = []
        
        for i in nums:
            d[i] = True
        
        for i in range(1, len(nums) + 1):
            if i in d:
                continue
            else:
                ans.append(i)
        
        return ans
