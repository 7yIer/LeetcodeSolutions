# https://leetcode.com/problems/index-pairs-of-a-string/
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # Brute force method
        ans = []
        for i in range(len(text)):
            for j in range(i, len(text) + 1):
                word = text[i:j]
                if word in words:
                    ans.append([i,j - 1])
        return ans
