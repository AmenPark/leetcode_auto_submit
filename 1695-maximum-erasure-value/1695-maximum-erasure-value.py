class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uset=set()
        lidx = 0
        N=len(nums)
        sums = 0
        ans = 0
        for ridx, num in enumerate(nums):
            while num in uset:
                sums -= nums[lidx]
                uset.remove(nums[lidx])
                lidx += 1
            uset.add(num)
            sums+=num
            ans=max(ans,sums)
        return ans