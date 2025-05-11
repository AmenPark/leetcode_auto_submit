class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod=10**9+7
        L=len(num)
        evens = (L+1)//2
        odds= L-evens
        cts=[0]*10
        s=0
        for n in num:
            n=int(n)
            cts[n] += 1
            s += n
        if s&1:
            return 0
        half = s//2
        s=0
        N = L + 1
        fac = [1] * N
        inv = [1] * N
        for i in range(1, N):
            fac[i] = fac[i - 1] * i % mod
        inv[N - 1] = pow(fac[N - 1], mod - 2, mod)
        for i in range(N - 2, -1, -1):
            inv[i] = inv[i + 1] * (i + 1) % mod

        dp={(0,0):1}
        for i in range(10):
            ndp = {}
            for k,v in dp.items():
                tg,c=k
                for j in range(cts[i]+1):
                    ndp[(tg,c)]=(ndp.get((tg,c),0)+ v* inv[j] * inv[cts[i]-j])%mod
                    tg+=i
                    c+=1
                    if c>evens:
                        break
            dp=ndp
        return (dp.get((half, evens),0)* fac[odds]*fac[evens])%mod