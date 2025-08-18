class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort()
        if nums[-1]<=0:
            return nums[-1]
        return sum({n for n in nums if n>0})