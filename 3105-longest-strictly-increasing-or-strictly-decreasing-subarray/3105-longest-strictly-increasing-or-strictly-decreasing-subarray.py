class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        s1 = 0
        s2 = 0
        bch = nums[0]
        ans = 1
        for n in nums:
            if n<bch:
                s1+=1
                s2 = 1
                ans = max(ans,s1)
            elif n>bch:
                s2 +=1
                s1 = 1
                ans = max(s2,ans)
            else:
                s1=1
                s2=1
            bch = n
        return ans