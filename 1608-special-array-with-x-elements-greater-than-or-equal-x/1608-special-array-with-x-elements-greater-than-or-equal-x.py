class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        for i,n in enumerate(nums):
            if (N-i) <= n:
                if i==0 or (nums[i-1] != n and nums[i-1] < N-i):
                    return N-i
                return -1
        return -1