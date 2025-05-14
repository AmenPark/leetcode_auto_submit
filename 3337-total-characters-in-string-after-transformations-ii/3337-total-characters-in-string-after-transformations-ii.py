class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod=10**9+7
        rec = {1:{}}
        for i in range(26):
            rec[1][i] = {j%26:1 for j in range(i+1,i+nums[i]+1)}
        
        def caseplus(rec1,rec2):
            rt = {}
            for i in range(26):
                rt[i] = {}
                for k,v in rec1[i].items():
                    for k2, v2 in rec2[k].items():
                        rt[i][k2] = (rt[i].get(k2,0) + v*v2)%mod
            return rt
        k=2
        hk = 1
        while k<=t:
            rec[k] = caseplus(rec[hk], rec[hk])
            hk=k
            k<<=1
        nr = rec[hk]
        k=hk//2
        while k:
            if hk+k<=t:
                nr = caseplus(nr, rec[k])
                hk += k
            k>>=1
        d = [0]*26
        for i in range(26):
            for key, val in nr[i].items():
                d[i] += val
                d[i]%=mod
        rt=0
        for ch in s:
            rt+=d[ord(ch)-ord('a')]
            rt%=mod
        return rt