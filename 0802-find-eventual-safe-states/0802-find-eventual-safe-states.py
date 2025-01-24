class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        counts = [0]*len(graph)
        rev = [[] for _ in graph]
        for i,ver in enumerate(graph):
            for v in ver:
                rev[v].append(i)
            counts[i]=len(ver)
        q = [i for i,val in enumerate(counts) if val==0]
        ans = []
        while q:
            ver = q.pop()
            ans.append(ver)
            for vertex in rev[ver]:
                counts[vertex]-=1
                if counts[vertex]==0:
                    q.append(vertex)

        ans.sort()
        return ans