class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ns = 0
        ans=0
        bv = nums[0]-1
        for n in nums:
            if n>bv:
                ns+=n
            else:
                ns=n
            ans=max(ans,ns)
            bv=n
        return ans