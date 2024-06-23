class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minl = collections.deque()
        maxl=collections.deque()
        ans=0
        nowl=-1
        for i,n in enumerate(nums):
            while minl and minl[-1][0] >= n:
                minl.pop()
            minl.append((n,i))
            while maxl and maxl[-1][0]<=n:
                maxl.pop()
            maxl.append((n,i))
            while n-minl[0][0]>limit:
                v,idx = minl.popleft()
                nowl=max(nowl,idx)
            while maxl[0][0]-n>limit:
                v,idx=maxl.popleft()
                nowl=max(nowl,idx)
            ans=max(ans, i-nowl)
        return ans
            