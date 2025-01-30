class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        conns = [[] for _ in range(n+1)]
        for x,y in edges:
            conns[x].append(y)
            conns[y].append(x)
        
        visited = [-1]*(n+1)
        def getRootAndSize(r):
            flags = [-1]*(n+1)
            q=[r]
            fnum=1
            flags[r]=1
            while q:
                nq=[]
                fnum+=1
                for nd in q:
                    for nnd in conns[nd]:
                        if flags[nnd]==-1:
                            flags[nnd]=fnum
                            visited[nnd]=0
                            nq.append(nnd)
                        elif abs(flags[nd]-flags[nnd])==1:
                            continue
                        else:
                            return -1,-1
                q=nq
            return fnum-1, nd
        ans=0
        for i in range(1,n+1):
            if visited[i]==-1:
                fnum, nd = getRootAndSize(i)
                if fnum==-1:
                    return -1
                fnum,nd = getRootAndSize(nd)
                ans+=fnum
        return ans