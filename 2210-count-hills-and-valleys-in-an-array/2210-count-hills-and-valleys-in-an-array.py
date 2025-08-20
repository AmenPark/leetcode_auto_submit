class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        N=len(nums)
        inc = None
        bn = nums[0]
        ans=0
        for n in nums:
            if n==bn:
                continue
            elif n>bn:
                if inc==False:
                    ans+=1
                inc=True
            elif n<bn:
                if inc==True:
                    ans+=1
                inc=False
            bn = n
        return ans