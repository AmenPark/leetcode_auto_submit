class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod=(10**9)+7
        #(n-1) choose k cases
        # multiply m*(m-1)**(not k cases)
        deval = 1
        for i in range(1,k+1):
            deval*=i
            deval%=mod
        val = 1
        for i in range(n-k,n):
            val*=i
            val%=mod
        rt= (pow(deval, mod-2, mod) * val)%mod
        rt*=pow(m-1,n-1-k,mod) * (m)
        return rt % mod