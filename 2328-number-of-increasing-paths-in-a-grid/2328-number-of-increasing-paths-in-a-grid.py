class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MODVAL=10**9+7
        N=len(grid)
        M=len(grid[0])
        board = [[-1 for _ in range(M)] for _ in range(N)]
        def getNeighbor(i,j):
            if i>0:
                yield i-1,j
            if i<N-1:
                yield i+1,j
            if j>0:
                yield i,j-1
            if j<M-1:
                yield i,j+1
        def getCount(i,j):
            if board[i][j]>-1:
                return board[i][j]
            v=grid[i][j]
            val=1
            for ni,nj in getNeighbor(i,j):
                if grid[ni][nj]<v:
                    val+=getCount(ni,nj)
            board[i][j]=val%MODVAL
            return val
        ans=0
        for i in range(N):
            for j in range(M):
                ans+=getCount(i,j)
                ans%=MODVAL
        return ans