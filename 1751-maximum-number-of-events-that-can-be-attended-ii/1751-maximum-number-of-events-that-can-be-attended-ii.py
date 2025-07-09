class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        hqs = [[] for _ in range(k)]
        nowvals = {k:0}
        for s,e,v in events:
            for i,hq in enumerate(hqs):
                if hq and hq[0][0]<s:
                    nowvals[i]=max(nowvals.get(i,0),heapq.heappop(hq)[1])
            for key in range(k,0,-1):
                if key not in nowvals:
                    break
                heapq.heappush(hqs[key-1],(e, nowvals[key]+v))
        for i,hq in enumerate(hqs):
            while hq:
                nowvals[i] = max(nowvals.get(i,0), heapq.heappop(hq)[1])
        return max(nowvals.values())