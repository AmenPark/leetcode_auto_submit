class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        N = len(words[0])
        M=len(target)
        chdic = [{} for _ in range(N)]
        for wd in words:
            for i,ch in enumerate(wd):
                chdic[i][ch] = chdic[i].get(ch,0)+1
        idxs = {}
        for i,ch in enumerate(target):
            if ch not in idxs:
                idxs[ch] = []
            idxs[ch].append(i)
        
        dp = {0:1}
        for dic in chdic:
            ndp = {}    
            for ch,ct in dic.items():
                for ind in idxs.get(ch,[]):
                    if dp.get(ind,0):
                        ndp[ind+1] = (ndp.get(ind+1,0) + ct * dp.get(ind,0))%MOD
            for k,v in dp.items():
                ndp[k]=(ndp.get(k,0)+v) % MOD
            dp = ndp
        return dp.get(len(target),0)%MOD