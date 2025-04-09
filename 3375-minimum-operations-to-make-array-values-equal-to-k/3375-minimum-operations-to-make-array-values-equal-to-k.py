class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1
        ans=0
        d[k]=0
        del d[k]
        for key,v in d.items():
            if key<k:
                return -1
            ans+=1
        return ans