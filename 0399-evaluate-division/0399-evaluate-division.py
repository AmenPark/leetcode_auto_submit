class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        conns = {}
        for (x,y),val in zip(equations, values):
            if x not in conns:
                conns[x]={}
            if y not in conns:
                conns[y]={}
            conns[x][y]=val
            conns[y][x]=1/val
        dic = {}
        keys = conns.keys()
        for key in keys:
            if key in dic:
                continue
            dic[key]=(key,1)
            q=[key]
            while q:
                nkey = q.pop()
                _, ct = dic[nkey]
                for nextkey, nextval in conns[nkey].items():
                    if nextkey in dic:
                        continue
                    dic[nextkey]=(key, nextval*ct)
                    q.append(nextkey)
        ans=[]
        for q,w in queries:
            if q not in dic:
                ans.append(-1.0)
            elif w not in dic:
                ans.append(-1.0)
            else:
                stq, qv = dic[q]
                stw, wv = dic[w]
                if stq!=stw:
                    ans.append(-1.0)
                else:
                    ans.append(wv/qv)
        return ans