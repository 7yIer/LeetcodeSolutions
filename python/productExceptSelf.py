class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # A product of everything except for itself is the product of everything to the left
        # and everything to the right
        # We can calculate this but first computing the product of everything to the right
        # and then we can calculate this by adding on to this product of everything to the left.
        
        leftProd = 1
        ans = []
        
        # Calculate everything on the left
        for num in nums:
            ans.append(leftProd)
            leftProd *= num
            
        
        rightProd = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= rightProd
            rightProd *= nums[i]
        
        return ans
