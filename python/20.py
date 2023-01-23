#[{}()[(()]]

class Solution:
    def isValid(self, s):
        stack = []
        m = {
            ")": "(",
            "}": "{",
            "]": '['
        }

        for c in s:
            if c in m:
                if stack and stack[-1] == m[c]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(c)

        return len(s) != 1 and len(stack) == 0

def main():
    s = "(())"
    res = Solution().isValid(s)
    print(res)
    return 0

if __name__ == "__main__":
    main()