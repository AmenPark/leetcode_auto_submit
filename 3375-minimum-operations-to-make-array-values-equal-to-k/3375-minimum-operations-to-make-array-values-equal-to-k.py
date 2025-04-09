class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ct=[0]*101
        for n in nums:
            ct[n]+=1
        ans=0
        for i in range(101):
            if ct[i]:
                if i<k:
                    return -1
                break
        ct[k]=0
        for i in range(101):
            if ct[i]==0:
                continue
            ans+=1

        return ans