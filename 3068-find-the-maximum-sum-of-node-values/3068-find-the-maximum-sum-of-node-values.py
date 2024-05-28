class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        S = sum(nums)
        mDiff = -k
        MDiff = k
        ct = 0
        flag=False
        for x in nums:
            diff = (x^k) - x
            if diff > 0:
                S += diff
                MDiff = min(MDiff, diff)
                ct^=1
            else:
                mDiff=max(mDiff,diff)
                flag=True
        if ct:
            ans = S-MDiff
            if flag:
                ans = max(ans, S+mDiff)
        else:
            ans = S
        return ans