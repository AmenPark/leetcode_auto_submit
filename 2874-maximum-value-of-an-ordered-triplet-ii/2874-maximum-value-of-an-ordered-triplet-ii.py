class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxval = 0
        maxdiff = 0
        ans = 0
        for n in nums:
            ans=max(maxdiff*n,ans)
            maxdiff=max(maxdiff, maxval-n)
            maxval=max(n,maxval)
        return ans