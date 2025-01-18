class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        N=len(grid)
        M=len(grid[0])
        def neighbors(x,y):
            if x>0:
                yield x-1,y, 4
            if y>0:
                yield x,y-1, 2
            if x<N-1:
                yield x+1,y, 3
            if y<M-1:
                yield x,y+1, 1
        costMap = [[10000 for _ in range(M)] for _ in range(N)]
        pq = [(0,(0,0))]
        costMap[0][0]=0
        while pq:
            cost, (x,y) = heapq.heappop(pq)
            if costMap[x][y]<cost:
                continue
            tdir=grid[x][y]
            for nx,ny,dir in neighbors(x,y):
                if dir==tdir:
                    ncost=cost
                else:
                    ncost=cost+1
                if costMap[nx][ny]>ncost:
                    costMap[nx][ny]=ncost
                    heapq.heappush(pq, (ncost, (nx, ny)))
        return costMap[-1][-1]


