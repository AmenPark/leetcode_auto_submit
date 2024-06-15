class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = {}
        N=40000
        def getdp(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i>=j-1:
                dp[(i,j)]=0
                return 0
            if i==j-2:
                dp[(i,j)]=i
                return i
            v=N
            for x in range(j-1,i-1,-1):
                nv = x+max(getdp(i,x), getdp(x+1,j))
                if nv>v:
                    dp[(i,j)]=v
                    return v
                v=nv
        return getdp(1,n+1)