class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        zct = 0
        for n in nums:
            if n==0:
                zct += 1
            else:
                ans += (zct*(zct+1))//2
                zct = 0
        ans += (zct*(zct+1))//2
        return ans        
        