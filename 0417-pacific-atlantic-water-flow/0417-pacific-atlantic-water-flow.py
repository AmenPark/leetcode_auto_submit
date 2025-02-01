class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        N=len(heights)
        M=len(heights[0])
        v = [[0 for _ in range(M)] for _ in range(N)]
        def getNeighbor(x,y):
            if x:
                yield x-1,y
            if y:
                yield x,y-1
            if x<N-1:
                yield x+1,y
            if y<M-1:
                yield x,y+1
        def search(x,y,flag):
            v[x][y]|=flag
            for nx,ny in getNeighbor(x,y):
                if heights[x][y]<=heights[nx][ny]:
                    if v[nx][ny]&flag==0:
                        search(nx,ny,flag)
        for i in range(N):
            search(i,0,1)
            search(i,M-1,2)
        for i in range(M):
            search(0,i,1)
            search(N-1,i,2)
        ans=[]
        for i in range(N):
            for j in range(M):
                if v[i][j]==3:
                    ans.append([i,j])
        return ans