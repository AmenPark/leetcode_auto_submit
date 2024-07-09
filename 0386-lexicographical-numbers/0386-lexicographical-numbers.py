class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l=[]
        now=1
        for _ in range(n):
            l.append(now)
            nnow=now*10
            if nnow > n:
                if now==n:
                    nnow = (now//10) + 1
                elif now%10==9:
                    nnow = now+1
                    while nnow%10 == 0:
                        nnow//=10
                else:
                    nnow=now+1
                
            
            now=nnow
        return l