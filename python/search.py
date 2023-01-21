# https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        
        while begin <= end:
            midpoint = begin + (end - begin) // 2
            val = nums[midpoint]
            
            if val == target:
                return midpoint
            elif target < val:
                end = midpoint - 1
            else:
                begin = midpoint + 1
        return -1
            
        
