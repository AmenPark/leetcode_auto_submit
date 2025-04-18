class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bits = 0
        ans = 0
        j = 0
        for i,n in enumerate(nums):
            if bits&n == 0:
                bits += n
                continue
            ans = max(ans, i-j)
            while bits&n:
                bits -= nums[j]
                j+=1
            bits += n
        ans=max(ans,len(nums)-j)
        return ans