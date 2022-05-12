# https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def omit(x):
            stack = []
            for i in x:
                if i != "#":
                    stack.append(i)
                else:
                    if len(stack) > 0:  
                        stack.pop()
            return ''.join(stack)
        return omit(s) == omit(t)
