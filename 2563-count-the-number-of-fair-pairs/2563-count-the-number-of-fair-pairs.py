class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans=0
        for i,n in enumerate(nums):
            if n>upper-n:
                break
            ridx = bisect_right(nums,upper-n)
            lidx=bisect_left(nums,lower-n)
            
            ans += ridx-max(lidx,i+1)

        return ans