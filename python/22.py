class Solution:
    def isValidParens(self, s):
        m = {")":"(","}":"{","]":"["}
        stack = []

        for c in s:
            if c in m:
                if stack and m[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0 and len(s) > 0

    def generateParenthesis(self, n):
        output = []
        def dfs(i=0, parens=""):
            if i == n * 2:
                print(parens)
                if self.isValidParens(parens):
                    print(parens)
                    nonlocal output
                    output.append(parens)
                return
            dfs(i + 1, parens + "(")
            dfs(i + 1, parens + ")")
        dfs()
        return output

def main():
    n = 3
    res = Solution().generateParenthesis(n)
    print(res)
    return 0

if __name__ == "__main__":
    main()