class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = [0]*(limit+1)
        ct = {}
        c = 0
        ans = []
        for x,y in queries:
            bc = colors[x]
            colors[x] = y
            if bc:
                ct[bc] -=1
                if ct[bc]==0:
                    c-=1
            if ct.get(y,0)==0:
                c+=1
            ct[y]=ct.get(y,0)+1
            ans.append(c)
        return ans
