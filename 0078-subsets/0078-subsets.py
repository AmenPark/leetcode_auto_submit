class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[nums[k] for k in range(len(nums)) if (1<<k)&i] for i in range(1<<len(nums))]