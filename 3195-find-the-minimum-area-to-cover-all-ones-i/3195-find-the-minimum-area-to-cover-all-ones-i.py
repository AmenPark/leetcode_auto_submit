class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        N=len(grid)
        M=len(grid[0])
        for i in range(N):
            if 1 in grid[i]:
                u=i
                break
        d=u
        for i in range(N-1,u,-1):
            if 1 in grid[i]:
                d=i
                break
        l=-1
        for j in range(M):
            for i in range(N):
                if grid[i][j]==1:
                    l=j
                    break
            if l>=0:
                break
        r=l
        for j in range(M-1,l,-1):
            for i in range(N):
                if grid[i][j]==1:
                    r=j
                    break
            if r>l:
                break
        return((r-l+1)*(d-u+1))