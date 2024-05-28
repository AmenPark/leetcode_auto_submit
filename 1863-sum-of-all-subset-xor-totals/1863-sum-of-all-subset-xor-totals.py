class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        i=1
        M = max(nums)
        ans = 0
        N = len(nums)
        while i<=M:
            ct = 0
            for n in nums:
                ct += ((n&i)>0)
            if ct==0:
                i<<=1
                continue
            ans += i <<(N-1)
            i<<=1
        return ans