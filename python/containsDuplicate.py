# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # A set is unique.
        # If the len of the set is not the same as nums, it must contain duplicates.
        return len(set(nums)) != len(nums)
