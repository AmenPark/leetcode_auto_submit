class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        l = []
        for st, et, val in events:
            l.append((st, 1, val))
            l.append((et, 2, val))
        l.sort()
        ans = 0
        maxEnd = 0
        for tm, tp, val in l:
            if tp==2:
                maxEnd = max(maxEnd, val)
            else:
                ans = max(ans, maxEnd+val)
        return ans