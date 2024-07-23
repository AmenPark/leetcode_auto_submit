class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ct={}
        for n in nums:
            ct[n]=ct.get(n,0)+1
        l=[(v,-k) for k,v in ct.items()]
        l.sort()
        ans=[]
        for v,k in l:
            ans.extend([-k]*v)
        return ans