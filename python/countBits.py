# https://leetcode.com/problems/counting-bits/
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Loop convert each i to binary, replace zeros, get length and store in an array
        ans = [0]
        for i in range(1,n+1):
            b = bin(i).replace("b", "").replace("0", "")
            ans.append(len(b))
        return ans
