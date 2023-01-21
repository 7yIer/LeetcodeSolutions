# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        nums.sort()
        return nums[len(nums) // 2]
        
        
        # Brute Force dictionary method
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums) // 2
        d = {}
        
        for num in nums:
            if num in d:
                d[num] += 1                
                if d[num] > n:
                    return num
            else:
                d[num] = 1
            
