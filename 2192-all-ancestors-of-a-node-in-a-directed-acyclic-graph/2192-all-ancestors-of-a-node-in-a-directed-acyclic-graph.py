class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        rt=[[] for _ in range(n)]
        conns=[[] for _ in range(n)]
        for x,y in edges:
            conns[x].append(y)
        v=[0]*n
        mark=1
        def dfs(i,mark,k):
            for nx in conns[i]:
                if v[nx]==mark:
                    continue
                v[nx]=mark
                rt[nx].append(k)
                dfs(nx,mark,k)
            
        for i in range(n):
            dfs(i,mark,i)
            mark+=1
        return rt