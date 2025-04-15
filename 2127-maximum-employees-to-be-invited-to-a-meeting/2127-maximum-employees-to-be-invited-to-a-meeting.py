class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N=len(favorite)
        hist = [[0,-1,-1,-1] for _ in range(N)]
        flag=1
        def search(flag, nd, before):
            nnd = favorite[nd]
            hist[nd][0]=flag
            if nnd==before:
                hist[nd] = [flag, 2, 2,before]
                return 1
            elif hist[nnd][0]==flag:
                hist[nd] = [flag, 1, 1,nd]
                hist[nnd][1]=1
                return 1
            elif hist[nnd][0]>0:
                if hist[nnd][1]==1:
                    hist[nd]=[flag,0,0,-1]
                    return 0
                elif hist[nnd][1]==2:
                    hist[nd]=[flag,2, hist[nnd][2]+1,hist[nnd][3]]
                    return hist[nnd][2]+1
                elif hist[nnd][1]==0:
                    hist[nd] = [flag,0,0,-1]
                    return 0

            else:
                l = search(flag, nnd, nd)
                if hist[nnd][1]==2:
                    if l==1:
                        hist[nd] = [flag,2,2,nnd]
                        return 2
                    hist[nd]=[flag, 2, l+1,hist[nnd][3]]
                    return l+1
                elif hist[nnd][1]==1:
                    if hist[nd][1]==1:
                        hist[nd]=[flag,1,l+1,hist[nnd][3]]
                        return -1
                    hist[nd]=[flag,1,l+1,hist[nnd][3]]
                    if l+1==0:
                        return -1
                    return l+1
                else:
                    hist[nd]=[flag,0,0,-1]
                    return 0
        for i in range(N):
            if hist[i][0]:
                continue
            search(flag,i,-1)
            flag+=1
        maxcycle = 0
        chains = {}
        for f, tp, n, lastnd in hist:
            if tp==0:
                continue
            if tp==1:
                maxcycle = max(maxcycle, n)
            elif tp==2:
                chains[lastnd] = max(chains.get(lastnd,0), n)
        ans=maxcycle
        ans=max(ans, sum(chains.values())-len(chains))
        return ans