class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        N=len(grid)
        M=len(grid[0])
        visited = [[0 for _ in range(M)] for _ in range(N)]

        def getNeighbor(x,y):
            if x:
                yield x-1,y
            if y:
                yield x,y-1
            if x<N-1:
                yield x+1,y
            if y<M-1:
                yield x,y+1

        def search(x,y):
            rt = grid[x][y]
            visited[x][y]=1
            for nx,ny in getNeighbor(x,y):
                if visited[nx][ny]:
                    continue
                if grid[nx][ny]==0:
                    continue
                rt += search(nx,ny)
            return rt
        ans=0
        for i in range(N):
            for j in range(M):
                if visited[i][j]:
                    continue
                if grid[i][j]==0:
                    continue
                ans=max(ans, search(i,j))
        return ans