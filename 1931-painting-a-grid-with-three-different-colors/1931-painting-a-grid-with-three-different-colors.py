class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9+7
        def getRow(val, depth):
            if depth==0:
                yield val
                return
            v=val<<3
            recval = val%8
            for i in [1,2,4]:
                if i==recval:
                    continue
                yield from getRow(v+i, depth-1)
        rowcases = [r for r in getRow(0,m)]
        dp = {0:1}
        for _ in range(n):
            ndp = {}
            for k,v in dp.items():
                for row in rowcases:
                    if k&row == 0:
                        ndp[row] = ndp.get(row,0)+v%MOD
            dp=ndp
        
        return sum(dp.values())%MOD