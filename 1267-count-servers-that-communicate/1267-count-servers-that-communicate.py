class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        N=len(grid)
        M=len(grid[0])
        rows=[0]*N
        cols=[0]*M
        for i,row in enumerate(grid):
            for j,val in enumerate(row):
                if val:
                    rows[i]+=1
                    cols[j]+=1
        ans=0
        for i,row in enumerate(grid):
            for j,val in enumerate(row):
                if val:
                    if rows[i]==1 and cols[j]==1:
                        continue
                    ans+=1
        return ans
                    

