class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ans = 0
        N=len(heightMap)
        M=len(heightMap[0])
        def getNeighbor(i,j):
            if i>0:
                yield(i-1,j)
            if j>0:
                yield(i,j-1)
            if i<N-1:
                yield(i+1,j)
            if j<M-1:
                yield(i,j+1)

        flagMap=[[0 for _ in range(M)] for _ in range(N)]
        repr = {0:0}
        areaInfos = {}
        heightInfos = {}
        isSideInfos = set()
        flag=1
        pos=[]
        def getFlag(i):
            if repr[i]==i:
                return i
            repr[i] = getFlag(repr[i])
            return repr[i]
        def unionFlag(i,j):
            ii = getFlag(i)
            jj = getFlag(j)
            if ii==jj:
                return
            m,M = min(ii,jj),max(ii,jj)
            areaInfos[m] += areaInfos[M]
            repr[M] = m
            

        for i,row in enumerate(heightMap):
            for j,val in enumerate(row):
                pos.append((val,i,j))
        pos.sort()
        for v,i,j in pos:
            isSide = False
            if i==0 or j==0 or i==N-1 or j==M-1:
                isSide=True
            nflag = flag
            repr[flag]=flag
            heightInfos[flag]=v
            areaInfos[flag]=1
            for ni,nj in getNeighbor(i,j):
                neflag = getFlag(flagMap[ni][nj])
                if neflag==0:
                    continue
                if neflag not in isSideInfos:
                    ans += areaInfos[neflag]*(v-heightInfos[neflag])
                else:
                    isSide=True
                unionFlag(neflag, nflag)
                nflag=getFlag(nflag)
                heightInfos[nflag]=v
            flag+=1
            if isSide:
                isSideInfos.add(nflag)
            flagMap[i][j]=nflag

        return ans