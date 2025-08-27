class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        N=len(grid)
        M=len(grid[0])
        rec = [[[0,0,0,0] for _ in range(M)] for _ in range(N)]
        directions = [(1,1), (1,-1), (-1,-1),(-1,1)]
        def getStart(x,y):
            for i,(dx,dy) in enumerate(directions):
                nx=x+dx
                ny=y+dy
                if 0<=nx<N and 0<=ny<M:
                    if grid[nx][ny]==2:
                        yield i, (nx,ny)
        def search(dir, fx,fy, mline):
            ans=searchline((dir+1)%4, fx, fy) + mline
            dx,dy = directions[dir]
            nx=fx+dx
            ny=fy+dy
            if not (0<=nx<N and 0<=ny<M):
                return ans
            if grid[fx][fy]+grid[nx][ny]!=2:
                return ans
            ans=max(ans, search(dir, nx,ny,mline+1))
            return ans

        
        def searchline(dir, fx, fy):
            if rec[fx][fy][dir]:
                return rec[fx][fy][dir]
            dx,dy = directions[dir]
            nx=fx+dx
            ny=fy+dy
            if not (0<=nx<N and 0<=ny<M):
                rec[fx][fy][dir]=1
                return 1
            if grid[fx][fy] + grid[nx][ny]!=2:
                rec[fx][fy][dir] = 1
                return 1
            rec[fx][fy][dir] = 1+searchline(dir, nx,ny)
            return rec[fx][fy][dir]
        ans=-1
        for i,row in enumerate(grid):
            for j,val in enumerate(row):
                if val==1:
                    ans=max(ans,0)
                    for dir, (fx,fy) in getStart(i,j):
                        ans=max(ans, search(dir, fx,fy,0))
        return ans+1