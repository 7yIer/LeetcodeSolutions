class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        l = 0
        r = 1
        
        while r < len(nums):
            if nums[l] == nums[r]:
                ans.append(nums[l])
                
            l += 1
            r += 1
            
        return ans
