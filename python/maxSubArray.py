# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Have a current sum
        # Have a maximum sum
        # Have a curr num that iterates
        # If the current number is ever bigger then the current sum
            # then we switch that to the current sum
        # Else
            # we add the value to the current sum and increment
        
        currentSum = maxSum = nums[0]
        curr = 1
        
        while curr < len(nums):
            currentSum = max(nums[curr], currentSum + nums[curr])
            maxSum = max(maxSum, currentSum)
            curr += 1
        return maxSum
