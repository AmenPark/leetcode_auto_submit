class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hq = []
        for p,c in zip(profits,capital):
            heapq.heappush(hq,(c,-p))
        ans = 0
        pools = []
        p,c = heapq.heappop(hq)
        for _ in range(k):
            while p<=w:
                heapq.heappush(pools,c)
                if hq:
                    p,c=heapq.heappop(hq)
                else:
                    p,c=0,0
                    break
            if not pools:
                break
            w -= heapq.heappop(pools)
        return w