class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        mdiff = 0
        maxval = 0
        ans=0
        for n in nums:
            ans = max(ans, mdiff*n)
            mdiff = max(mdiff, maxval - n)
            maxval = max(maxval,n)
        return ans