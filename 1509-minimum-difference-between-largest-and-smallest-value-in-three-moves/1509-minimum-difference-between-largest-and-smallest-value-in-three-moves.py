class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if N<=4:
            return 0
        l = sorted(nums)
        return min(l[-1]-l[3], l[-2]-l[2], l[-3]-l[1], l[-4]-l[0])