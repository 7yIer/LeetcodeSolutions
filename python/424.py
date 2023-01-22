class Solution:
    def characterReplacement(self, s, k):
        l, r = 0, 0
        charCount = {}
        maxCount = 0
        output = 0

        for r in range(len(s)):
            c = s[r]
            charCount[c] = charCount.get(c, 0) + 1
            maxCount = max(maxCount, charCount[c])

            if r - l - maxCount + 1 > k:
                c = s[l]
                charCount[c] -= 1
                l += 1
            
            output = max(output, r - l + 1)


        return output
    

def main():
    s = "AABABBA"
    k = 1
    res = Solution().characterReplacement(s, k)
    print(res)

    return 0

if __name__ == "__main__":
    main()