class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        tg = (s+1)//2
        ans=-1
        ss=0
        if tg<=0:
            ans+=1
        for n in nums:
            ss+=n
            if ss>=tg:
                ans+=1
        return ans
        