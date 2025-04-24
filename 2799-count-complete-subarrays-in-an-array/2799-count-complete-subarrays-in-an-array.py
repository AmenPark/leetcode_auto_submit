class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cts = {i:0 for i in nums}
        flag = len(cts)
        j=0
        ans = 0
        N=len(nums)
        for i,num in enumerate(nums):
            if cts[num]==0:
                flag -=1
            cts[num]+=1
            while flag == 0 :
                ans += N-i
                cts[nums[j]] -= 1
                if cts[nums[j]]==0:
                    flag +=1
                j+=1
        return ans