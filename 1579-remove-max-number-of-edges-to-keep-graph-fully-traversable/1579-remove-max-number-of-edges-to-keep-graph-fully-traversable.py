class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def getrep(rep,i):
            if rep[i]==i:
                return rep[i]
            rep[i]=getrep(rep,rep[i])
            return rep[i]
        def unirep(rep,i,j):
            i=getrep(rep,i)
            j=getrep(rep,j)
            if i==j:
                return True
            v=min(i,j)
            rep[i]=v
            rep[j]=v
            return False
        rep=[i for i in range(n+1)]
        alice=[i for i in range(n+1)]
        bob=[i for i in range(n+1)]
        ans=0
        for tp,u,v in edges:
            if tp==3:
                if unirep(rep,u,v):
                    ans+=1
                else:
                    if unirep(alice,u,v):
                        ans+=1
                    if unirep(bob,u,v):
                        ans+=1
            elif tp==2:
                if unirep(alice,u,v):
                    ans+=1
            else:
                if unirep(bob,u,v):
                    ans+=1
            
        for i in range(2,n+1):
            if getrep(alice,i)!=1:
                return -1
            if getrep(bob,i)!=1:
                return -1
        return ans