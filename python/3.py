class Solution:
    def lengthOfLongestSubstring(self, s):
        # abcabcbb
        distinctSubstring = set()
        l, r = 0, 0
        output = 0
        for r in range(len(s)):
            c = s[r]
            while c in distinctSubstring:
                distinctSubstring.remove(s[l])
                l += 1
            distinctSubstring.add(s[r])
            output = max(output, r - l + 1)
        return output

def main():
    s = "abcabcbb"
    res = Solution().lengthOfLongestSubstring(s)
    print(res)
    return 0

if __name__ == "__main__":
    main()