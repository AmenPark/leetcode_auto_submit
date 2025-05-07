class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N=len(moveTime)
        M=len(moveTime[0])
        hq=[]
        v=[[-1 for _ in range(M)] for _ in range(N)]
        v[0][0]=0
        def getN(x,y):
            if x:
                yield x-1,y
            if y:
                yield x,y-1
            if x<N-1:
                yield x+1,y
            if y<M-1:
                yield x,y+1
        heapq.heappush(hq,(0,0,0))
        while hq:
            t,x,y = heapq.heappop(hq)
            for nx, ny in getN(x,y):
                if v[nx][ny]>=0:
                    continue
                nt = max(t, moveTime[nx][ny])+1
                heapq.heappush(hq, (nt, nx, ny))
                v[nx][ny] = nt
        return v[-1][-1]