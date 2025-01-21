class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        usum = sum(grid[0])
        usum -= grid[0][0]
        ans=max(0,usum)
        dsum=0
        for i in range(1,len(grid[0])):
            usum -= grid[0][i]
            dsum += grid[1][i-1]
            ans=min(max(usum,dsum),ans)
        return ans
