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

        def fill_check(fills,flag):
            while fills:
                nf = []
                for x,y in fills:
                    for ni, nj in getNeighbor(x,y):
                        if checker[ni][nj]==1 or checker[ni][nj]==flag:
                            continue
                        nf.append((ni,nj))
                        checker[ni][nj]=flag
                fills=nf
                
        hq = []
        checker = [[0 for _ in range(M)] for _ in range(N)]
        for i,row in enumerate(heightMap):
            for j,val in enumerate(row):
                heapq.heappush(hq, (-val,i,j))
        flag = -1
        while hq:
            nval = hq[0][0]
            while hq and nval==hq[0][0]:
                _,i,j = heapq.heappop(hq)
                checker[i][j]=1
            
            height = -nval
            for i in range(N):
                if checker[i][0]==flag or checker[i][0]==1:
                    continue
                fills = [(i,0)]
                checker[i][0]=flag
                fill_check(fills,flag)

            for j in range(M):
                if checker[0][j] == flag or checker[0][j] == 1:
                    continue
                fills=[(0,j)]
                checker[0][j]=flag
                fill_check(fills,flag)

            for i in range(N):
                if checker[i][M-1]==flag or checker[i][M-1]==1:
                    continue
                fills = [(i,M-1)]
                checker[i][M-1]=flag
                fill_check(fills,flag)

            for j in range(M):
                if checker[N-1][j] == flag or checker[N-1][j] == 1:
                    continue
                fills=[(N-1,j)]
                checker[N-1][j]=flag
                fill_check(fills,flag)

            for i,row in enumerate(checker):
                for j,val in enumerate(row):
                    if val == flag+1:
                        ans += height - heightMap[i][j]
            flag-=1
        return ans