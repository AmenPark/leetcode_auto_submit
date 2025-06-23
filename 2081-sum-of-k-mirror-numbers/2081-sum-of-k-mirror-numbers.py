class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def get10mirrors():
            for i in range(1,10):
                yield i
            halfMIN=1
            halfMAX=10
            # 1~9 , 10~99, 100~999, ...
            while True:
                for half in range(halfMIN, halfMAX):
                    val=str(half)
                    val += val[::-1]
                    yield int(val)
                for half in range(halfMIN, halfMAX):
                    val=str(half)
                    for mid in range(0,10):
                        mval =val + str(mid)
                        yield int(mval+val[::-1])
                halfMIN*=10
                halfMAX*=10
        def toKmirrors(k, val):
            rt = []
            while val:
                rt.append(val%k)
                val//=k
            return rt
        def checkMirror(l):
            N=len(l)
            for i in range(N//2):
                if l[i]!=l[-i-1]:
                    return False
            return True
        m10s = get10mirrors()
        ans=0
        ct=0
        while ct<n:
            val=next(m10s)
            if checkMirror(toKmirrors(k,val)):
                ct+=1
                ans+=val
        return ans