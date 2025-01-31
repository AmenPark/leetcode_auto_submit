class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N=len(matrix)
        M=len(matrix[0])
        hq = [(matrix[0][0],(0,0))]
        for _ in range(k-1):
            v,(x,y) = heapq.heappop(hq)
            if x<N-1:
                heapq.heappush(hq, (matrix[x+1][y],(x+1,y)))
            if y<M-1:
                heapq.heappush(hq,(matrix[x][y+1],(x,y+1)))
        v,_ = heapq.heappop(hq)
        return v