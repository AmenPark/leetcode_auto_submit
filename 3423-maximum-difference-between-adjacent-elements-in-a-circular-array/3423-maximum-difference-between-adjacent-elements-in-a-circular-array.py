class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        bval = nums[-1]
        ans=0
        for n in nums:
            ans=max(ans, abs(n-bval))
            bval=n
        return ans