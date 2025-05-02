class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N=len(grid)
        rt=[-1,-1]
        for i in range(N):
            for j in range(N):
                v=grid[i][j] - 1
                tg=i*N + j
                while v!=tg:
                    ch = grid[v//N][v%N] - 1
                    if ch==v:
                        return [ch+1,tg+1]
                    grid[v//N][v%N] = v + 1
                    grid[i][j]=ch+1
                    v=ch
                

