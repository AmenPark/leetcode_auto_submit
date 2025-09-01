class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        hq = []
        N=len(classes)
        ss = 0
        for a,b in classes:
            heapq.heappush(hq, (a/b-(a+1)/(b+1), b,a))
            ss += a/b
        for _ in range(extraStudents):
            v,b,a = heapq.heappop(hq)
            ss -= v
            b+=1
            a+=1
            heapq.heappush(hq,(a/b-(a+1)/(b+1), b,a))
        return ss/N