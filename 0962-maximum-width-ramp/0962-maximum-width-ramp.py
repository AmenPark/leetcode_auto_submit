class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        l = [(n,i) for i,n in enumerate(nums)]
        l.sort()
        bm = len(l)
        ans = 0
        for n,i in l:
            ans = max(ans, i-bm)
            bm=min(bm, i)
        return ans