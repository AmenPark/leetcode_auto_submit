class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans=0
        brow = [0]*len(mat[0])
        for row in mat:
            addval = 0
            hq = [0]
            cts={}
            for i,val in enumerate(row):
                if val==0:
                    row[i] = 0
                    addval=0
                    cts={}
                    heights_hq=[0]
                else:
                    nval = brow[i]+1
                    row[i] = nval
                    if -hq[0] < nval:
                        heapq.heappush(hq, -nval)
                    if -hq[0]==nval:
                        addval += nval
                        cts[nval]=cts.get(nval,0)+1
                        ans += addval
                    else:
                        while -hq[0] > nval:
                            overval = -heapq.heappop(hq)
                            overvalct = cts[overval]
                            addval -= (overval - nval) * overvalct
                            del cts[overval]
                            cts[nval]=cts.get(nval,0)+overvalct
                        cts[nval]=cts.get(nval,0)+1
                        addval+=nval
                        ans+=addval
            brow = row
                
        return ans