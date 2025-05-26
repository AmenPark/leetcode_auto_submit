class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N=len(colors)
        v=[0]*N
        conns = [[] for _ in range(N)]
        for a,b in edges:
            conns[a].append(b)
        cts = [[0 for _ in range(26)] for _ in range(N)]
        roots = set()
        def search(nd):
            ndc = ord(colors[nd])-ord('a')
            v[nd]=2
            for nnd in conns[nd]:
                roots.discard(nnd)
                assert v[nnd]!=2
                if v[nnd]==0:
                    search(nnd)
                for i in range(26):
                    cts[nd][i] = max(cts[nd][i], cts[nnd][i])
            cts[nd][ndc]+=1
            v[nd]=1
        for nd in range(N):
            try:
                if v[nd]==0:
                    roots.add(nd)
                    search(nd)
            except AssertionError:
                return -1
        ans=0
        for root in roots:
            ans=max(ans, max(cts[root]))
        return ans