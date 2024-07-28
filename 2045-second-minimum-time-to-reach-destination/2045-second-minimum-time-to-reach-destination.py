class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        conn = [[] for _ in range(n+1)]
        for x,y in edges:
            conn[x].append(y)
            conn[y].append(x)
        ve=[-1]*(n+1)
        vo=[-1]*(n+1)
        vo[1]=0
        now=[1]
        t=0
        while now:
            t+=1
            nnow=[]
            vo,ve = ve,vo
            for nd in now:
                for nnd in conn[nd]:
                    if vo[nnd]==-1:
                        vo[nnd]=t
                        nnow.append(nnd)
            now=nnow
        a1=vo[-1]
        a2=ve[-1]
        M,m = max(a1,a2), min(a1,a2)
        if m==-1:
            tg=M+2
        else:
            tg=min(M,m+2)
        N=change*2
        mod = time%N
        if mod==0:
            return time*tg
        mov = 1+((change-1)//mod)
        startgap =(1+((mov*time-1)//N)) * N
        cycles = (tg-1)//mov
        return cycles*startgap + (tg-cycles*mov)*time