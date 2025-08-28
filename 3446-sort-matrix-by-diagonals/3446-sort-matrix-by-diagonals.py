class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N=len(grid)
        M=len(grid[0])
        for i in range(N):
            l = [grid[i+k][k] for k in range(min(N-i,M))]
            l.sort(reverse=True)
            for k in range(min(N-i,M)):
                grid[i+k][k] = l[k]
        for j in range(1,M):
            l=[grid[k][j+k] for k in range(min(N,M-j))]
            l.sort()
            for k in range(min(N,M-j)):
                grid[k][j+k]=l[k]
        return grid