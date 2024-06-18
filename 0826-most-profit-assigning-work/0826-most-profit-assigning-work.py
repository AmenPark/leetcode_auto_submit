class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        hq = []
        for d,p in zip(difficulty,profit):
            heapq.heappush(hq,(d,p))
        worker.sort()
        ans=0
        mprofit = 0
        d,p=heapq.heappop(hq)
        for w in worker:
            while True:
                if d<=w:
                    mprofit=max(mprofit,p)
                    if not hq:
                        break
                    d,p=heapq.heappop(hq)
                else:
                    break
            ans += mprofit
        return ans
