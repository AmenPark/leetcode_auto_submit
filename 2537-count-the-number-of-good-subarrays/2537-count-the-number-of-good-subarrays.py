class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ct = {}
        pairs = 0
        ans = 0
        j=0
        N=len(nums)
        for i,num in enumerate(nums):
            pairs += ct.get(num,0)
            ct[num]=ct.get(num,0)+1
            while pairs>=k:
                ans += N-i
                pairs -= ct.get(nums[j],0)-1
                nums[j] -=1
                j+=1
        return ans
