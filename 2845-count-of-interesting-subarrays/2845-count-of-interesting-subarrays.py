class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cts = {}
        ss = 0
        cts[0] = 1
        ans=0
        for n in nums:
            val = int((n%modulo)==k)
            ss+=val
            ss%=modulo
            ans += cts.get((ss-k)%modulo,0)
            cts[ss]= cts.get(ss,0)+1
        return ans