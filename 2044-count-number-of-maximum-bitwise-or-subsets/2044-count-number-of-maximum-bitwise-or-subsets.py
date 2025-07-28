class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        cts = {0:1}
        for n in nums:
            nct={}
            for k,v in cts.items():
                nct[k|n] = nct.get(k|n,0)+v
                nct[k]=nct.get(k,0)+v
            cts=nct
        return max(cts.values())