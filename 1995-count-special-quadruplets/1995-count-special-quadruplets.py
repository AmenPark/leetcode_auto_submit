class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        oct = {}
        cct = {}
        trct = {}
        ans=0
        for n in nums:
            ans += trct.get(n,0)
            for k,v in cct.items():
                trct[k+n]=trct.get(k+n,0)+v
            for k,v in oct.items():
                cct[k+n] = cct.get(k+n,0)+v
            oct[n] = oct.get(n,0)+1
        return ans