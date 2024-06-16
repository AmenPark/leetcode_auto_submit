class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        rangeend = 0
        i=0
        N=len(nums)
        while rangeend < n:
            target = rangeend+1
            if i==N or target < nums[i]:
                ans += 1
                rangeend += target
            else:
                rangeend += nums[i]
                i+=1
        return ans