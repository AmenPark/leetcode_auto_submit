class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if k*m > len(bloomDay):
            return -1
        d = {}
        hq = []
        
        for i,b in enumerate(bloomDay):
            if b not in d:
                d[b]=[]
                heapq.heappush(hq,b)
            d[b].append(i)
        starts={}
        ends={}
        nowk = 0
        while hq:
            day = heapq.heappop(hq)
            for pos in d[day]:
                if pos-1 in starts:
                    start=starts[pos-1]
                    if pos+1 in ends:
                        end=ends[pos+1]
                        nowk -= (end-pos)//k + (pos - start)//k
                        del starts[pos-1]
                        del ends[pos+1]
                        starts[end] = start
                        ends[start] = end
                        nowk += (end - start + 1)//k
                        continue
                    nowk -= (pos-start)//k
                    del starts[pos-1]
                    starts[pos]=start
                    ends[start]=pos
                    nowk+=(pos-start+1)//k
                    continue
                if pos+1 in ends:
                    end=ends[pos+1]
                    nowk-=(end-pos)//k
                    del ends[pos+1]
                    ends[pos]=end
                    starts[end]=pos
                    nowk+=(end-pos+1)//k
                    continue
                starts[pos]=pos
                ends[pos]=pos
                if k==1:
                    nowk+=1 
            if nowk>=m:
                break
        return day