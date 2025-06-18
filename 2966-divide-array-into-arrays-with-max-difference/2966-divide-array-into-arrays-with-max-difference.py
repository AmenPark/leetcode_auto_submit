class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        N=len(nums)
        for i in range(2,N,3):
            if nums[i]-nums[i-2]>k:
                return []
        return [nums[i:i+3] for i in range(0,N,3)]