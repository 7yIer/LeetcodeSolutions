from collections import Counter
from math import inf

class Solution:
    def minWindow(self, s, t):
        if t == "":
            return ""
        tCount = Counter(t)
        sCount = {}
        l = 0
        d = [0, len(s)]
        delta = inf

        matches, desiredMatches = 0, len(tCount)
        for r in range(len(s)):
            c = s[r]
            sCount[c] = sCount.get(c, 0) + 1

            if c in tCount and sCount[c] == tCount[c]:
                matches += 1

            while matches == desiredMatches:
                if (r - l + 1) <= delta:
                    d = [l, r]
                    delta = r - l + 1
                
                c = s[l]
                sCount[c] -= 1
                if sCount[c] == tCount[c] - 1:
                    matches -= 1
                l += 1

        return s[d[0]:d[1] + 1] if delta != inf else ""

def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    res = Solution().minWindow(s,t)
    print(res)
    return 0


if __name__ == "__main__":
    main()