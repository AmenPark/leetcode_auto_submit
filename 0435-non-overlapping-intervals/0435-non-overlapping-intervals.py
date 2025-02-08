class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        till=intervals[0][0]-1
        ans = 0
        for x,y in intervals:
            if till<=x:
                till = y
            else:
                ans+=1
                till=min(till,y)
        return ans