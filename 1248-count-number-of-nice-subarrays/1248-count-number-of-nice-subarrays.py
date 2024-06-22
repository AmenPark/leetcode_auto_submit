class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        s=1
        l=[]
        for n in nums:
            if n&1:
                l.append(s)
                s=0
            s+=1
        l.append(s)
        ans = 0
        for x,y in zip(l,l[k:]):
            ans+=x*y
        return ans