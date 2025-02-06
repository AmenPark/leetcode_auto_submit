class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        tval = {}
        N=len(nums)
        for i in range(N):
            for j in range(i+1,N):
                val=nums[i]*nums[j]
                ans += tval.get(val,0)
                tval[val] = tval.get(val,0)+1
        return ans*8