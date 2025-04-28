class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        N=len(nums)
        i=0
        j=0
        ss=0
        while j<N:
            if ss*(i-j)<k:
                if i<N:
                    ss += nums[i]
                    i+=1
                else:
                    ans += i-j
                    ss -= nums[j]
                    j+=1
            else:
                ans += i-j-1
                ss -= nums[j]
                j+=1
        return ans