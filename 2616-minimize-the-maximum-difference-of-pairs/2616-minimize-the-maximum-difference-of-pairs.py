class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if not nums:
            return 0
        if p==0:
            return 0
        nums.sort()
        N=len(nums)
        def countUnderDiff(diff):
            ct=0
            i=0
            while i<N-1:
                if nums[i+1]-nums[i]<=diff:
                    ct+=1
                    i+=2
                else:
                    i+=1
            return ct
        if countUnderDiff(0)>=p:
            return 0
        l=0
        r=nums[-1]-nums[0]
        while l<r-1:
            m=(l+r)//2
            if countUnderDiff(m)>=p:
                r=m
            else:
                l=m
        return r
