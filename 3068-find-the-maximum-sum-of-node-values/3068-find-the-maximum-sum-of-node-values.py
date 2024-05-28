class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        S = sum(nums)
        mDiff = -k
        MDiff = k
        ct = 0
        for x in nums:
            diff = (x^k) - x
            if diff > 0:
                S += diff
                MDiff = min(MDiff, diff)
                ct^=1
            else:
                mDiff=max(mDiff,diff)
        if ct:
            return max(S-MDiff, S+mDiff)
        else:
            return S