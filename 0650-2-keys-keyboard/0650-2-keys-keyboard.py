class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        p = {}
        primes = [2]
        tg=3

        while n%2==0:
            p[2]=p.get(2,0)+1
            n//=2
        
        def isprime(tg,primes):
            for p in primes:
                if tg%p == 0:
                    return False
            return True
        while tg<=n:
            if isprime(tg,primes):
                primes.append(tg)
                while n%tg==0:
                    p[tg]=p.get(tg,0)+1
                    n//=tg
            tg+=2
        ans=0
        for k,v in p.items():
            ans += (k)**v
        return ans