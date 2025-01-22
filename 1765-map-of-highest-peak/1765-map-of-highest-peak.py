class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        N=len(isWater)
        M=len(isWater[0])
        ans = [[-1 for _ in range(M)]for _ in range(N)]
        def getNeighbor(x,y):
            if x>0:
                yield x-1,y
            if y>0:
                yield x,y-1
            if x<N-1:
                yield x+1,y
            if y<M-1:
                yield x,y+1
        nowq = []
        for i,row in enumerate(isWater):
            for j,val in enumerate(row):
                if val==1:
                    nowq.append((i,j))
                    ans[i][j]=0
        flag=0
        while nowq:
            flag+=1
            nextq = []
            for i,j in nowq:
                for nx,ny in getNeighbor(i,j):
                    if ans[nx][ny]==-1:
                        ans[nx][ny]=flag
                        nextq.append((nx,ny))
            nowq=nextq
        return ans