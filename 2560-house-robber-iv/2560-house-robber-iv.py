class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N=len(nums)
        def guess(k):
            ct=0
            i=0
            while i<N:
                if nums[i]<=k:
                    ct+=1
                    i+=1
                i+=1
            return ct
        l=0
        r=10**9
        while l<r-1:
            m=(l+r)//2
            if guess(m)>=k:
                r=m
            else:
                l=m
        return r