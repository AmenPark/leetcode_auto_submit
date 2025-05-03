class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1]*len(queries)
        l = []
        for idx,(x,y) in enumerate(queries):
            if x<y and heights[x]<heights[y]:
                ans[idx]=y
            elif x>y and heights[x]>heights[y]:
                ans[idx] = x
            elif x==y:
                ans[idx]=x
            else:
                l.append((max(x,y), max(heights[x], heights[y])+1, idx))
        hq = []
        l.sort()
        i=0
        for buildingpos, bound, idx in l:

            while i<buildingpos and hq:
                if heights[i] >= hq[0][0]:
                    ans[hq[0][1]] = i
                    heapq.heappop(hq)
                else:
                    i+=1
            i=buildingpos
            heapq.heappush(hq, (bound, idx))
        while i<len(heights) and hq:
            if heights[i] >= hq[0][0]:
                ans[hq[0][1]] = i
                heapq.heappop(hq)
            else:
                i+=1
        return ans

