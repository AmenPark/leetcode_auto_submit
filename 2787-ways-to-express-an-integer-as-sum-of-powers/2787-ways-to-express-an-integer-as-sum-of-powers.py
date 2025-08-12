class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = {n:1}
        i=1
        MOD=10**9+7
        while True:
            val = i**x
            if val>n:
                break
            ndp = {}
            for k,v in dp.items():
                ndp[k]= ndp.get(k,0) + v
                if k-val>=0:
                    ndp[k-val] = (ndp.get(k-val,0)+v)%MOD
            dp=ndp
            i+=1
        return dp.get(0,0)%MOD
