# https://leetcode.com/problems/two-sum/submissions/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in d:
                return [d[target-num], i]
            d[num] = i
        
