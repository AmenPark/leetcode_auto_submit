class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ct=0
        maxval=0
        ans=1
        for n in nums:
            if n>maxval:
                maxval=n
                ans=1
                ct=1
            elif n==maxval:
                ct+=1
                ans=max(ans,ct)
            else:
                ct=0
        return ans