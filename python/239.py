import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
        return output

def main():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    res = Solution().maxSlidingWindow(nums, k)
    print(res)
    return 0

if __name__ == "__main__":
    main()