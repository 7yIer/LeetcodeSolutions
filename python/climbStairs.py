# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci Numbers | n
        # F0 = 0
        # F1 = 1
        # F2 = 1
        # F3 = 2 | n = 2
        # F4 = 3 | n = 3
        
        # From these fibonacci numbers we can draw the relationship
        # that for n stairs there are Fn+1 number of ways to climb them.
        
        # From the logic above, we need to create a fibonacci function that returns n + 1
        
        # Solution 1:
        # This solution was not optimal because recursion is too slow.
        def fib(n):
            if n in {0, 1}:
                return n
            return fib(n - 1) + fib(n - 2)
        
        return fib(n+1)
    
        # Solution 2:
        # This solution uses the equation for fibonacci numbers.
        def fib(n):
            return math.floor((((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5)))
        
        return fib(n+1)
