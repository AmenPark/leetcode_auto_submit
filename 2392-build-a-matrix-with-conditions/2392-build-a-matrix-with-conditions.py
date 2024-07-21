class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(k)] for _ in range(k)]
        def findarr(conditions):
            conns=[set() for _ in range(k+1)]
            for l,r in conditions:
                conns[r].add(l)
            depths=[-1]*(k+1)
            v=[0]*(k+1)
            cf=[False]
            def getdepths(i):
                if v[i]==1:
                    cf[0]=True
                    return depths[i]
                elif v[i]==2:
                    return depths[i]
                v[i]=1
                md=-1
                for c in conns[i]:
                    md=max(md,getdepths(c))
                depths[i]=md+1
                v[i]=2
                return depths[i]
            for i in range(1,k+1):
                getdepths(i)
            return *cf, depths
        cf1, rowcd = findarr(rowConditions)
        cf2, colcd = findarr(colConditions)
        if cf1 or cf2:
            return []
        def getps(cd):
            rt = {}
            for i,n in enumerate(cd[1:],1):
                if n not in rt:
                    rt[n]=[]
                rt[n].append(i)
            arr=rt[0]
            for i in range(1,k+1):
                if rt.get(i,None)==None:
                    break
                arr.extend(rt[i])
            rt = [0]*(k+1)
            for i,n in enumerate(arr):
                rt[n]=i
            return rt
        rps=getps(rowcd)
        cps=getps(colcd)
        for i in range(1,k+1):
            ii=rps[i]
            jj=cps[i]
            ans[ii][jj]=i
        
        return ans