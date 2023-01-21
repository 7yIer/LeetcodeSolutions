# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Loop through letters
        # If the ASCII of the letter is greater than the ASCII of target
            # Return that letter
        # No letter found, return the first letter

        for i in letters:
            if i > target:
                return i
        return letters[0]
