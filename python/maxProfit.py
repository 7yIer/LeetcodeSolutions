# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force algo
        # Loop over the nums at 0 to n - 1
            # Loop over the nums at i to n
                # Compare for max profit
        
        maxProfit = 0
        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                currentProfit = prices[j] - prices[i]
                
                if currentProfit > maxProfit:
                    maxProfit = currentProfit
        return maxProfit
    
        # Two pointer algo
        # Have a left and a right
        # If right < left then left becomes right and right + 1
        # Else calculate the profit and set the max
        # Until right hits the end
        
        if len(prices) == 1:
            return 0
        
        l = 0
        r = 1
        maxProfit = 0
        
        while r < len(prices):
            leftPrice = prices[l]
            rightPrice = prices[r]
            
            if leftPrice > rightPrice:
                l = r
                r += 1
            else:
                currProfit = rightPrice - leftPrice
                maxProfit = max(maxProfit, currProfit)
                r += 1
        
        return maxProfit
                
                    
                
    
        
