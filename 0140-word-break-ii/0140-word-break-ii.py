class Solution:
    def findans(self, s, nowidx, conn, now):
        if nowidx == 0:
            self.ans.append(" ".join(now[::-1]))
            return
        for nextidx in conn[nowidx]:
            now.append(s[nextidx:nowidx])
            self.findans(s,nextidx,conn,now)
            now.pop()
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ws = set(wordDict)
        N = len(s)
        conn = [[] for _ in range(N+1)]
        for i in range(N):
            for j in range(i+1,min(N+1, i+11)):
                wd = s[i:j]
                if wd in ws:
                    conn[j].append(i)
        self.ans = []
        self.findans(s,N,conn,[])
        return self.ans