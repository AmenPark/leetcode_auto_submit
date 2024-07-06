class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        conn=[set() for _ in range(n+1)]
        for x,y in edges:
            conn[x].add(y)
            conn[y].add(x)
        evens=[]
        for i in range(1,n+1):
            if len(conn[i])%2 == 1:
                evens.append(i)
        if len(evens)>4:
            return False
        if not evens:
            return True
        if len(evens)==4:
            e1,e2,e3,e4 = evens
            if e1 not in conn[e2]:
                if e3 not in conn[e4]:
                    return True
            if e1 not in conn[e3]:
                if e2 not in conn[e4]:
                    return True
            if e1 not in conn[e4]:
                if e2 not in conn[e3]:
                    return True
            return False
        
        e1,e2 = evens
        if e1 not in conn[e2]:
            return True
        s = {i for i in range(1,n+1)}
        xs = set()
        for i in conn[e1]:
            xs.add(i)
        for i in conn[e2]:
            xs.add(i)
        for i in xs:
            s.remove(i)
        for i in s:
            if i!=e1 and i!=e2:
                return True
        return False