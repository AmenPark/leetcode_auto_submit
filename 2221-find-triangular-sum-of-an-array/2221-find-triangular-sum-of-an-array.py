class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N=len(nums)
        for i in range(N-1,-1,-1):
            for j in range(i):
                nums[j] = (nums[j]+nums[j+1])%10
        return nums[0]