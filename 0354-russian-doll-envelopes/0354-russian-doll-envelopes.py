class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        d={}
        keys = []
        for x,y in envelopes:
            if x not in d:
                d[x] = []
                heapq.heappush(keys,x)
            heapq.heappush(d[x],-y)
        nows = []
        N=0
        while keys:
            print(nows)
            w = heapq.heappop(keys)
            tg = d[w]
            print("==", tg)
            br=N-1
            bh = -tg[0]+1
            while tg:
                h = -heapq.heappop(tg)
                if bh==h:
                    continue
                bh = h
                l=0
                r=br
                if N==0 or h>nows[-1]:
                    nows.append(h)
                    N+=1
                    br+=1
                    continue
                if h<=nows[0]:
                    nows[0] = h
                    continue
                while l<r-1:
                    mid = (l+r)//2
                    if nows[mid]<h:
                        l=mid
                    else:
                        r=mid
                nows[r]=h
                br = r
        return N
