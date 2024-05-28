class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        hq = []
        for x,y in zip(s,t):
            heapq.heappush(hq, abs(ord(x)-ord(y)))
        c = 0
        ans = 0
        while hq:
            c+= heapq.heappop(hq)
            if c>maxCost:
                break
            ans+=1
        return ans