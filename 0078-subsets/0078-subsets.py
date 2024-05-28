class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1<<len(nums)):
            ans.append([nums[k] for k in range(len(nums)) if (1<<k)&i])
        return ans