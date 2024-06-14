class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        uf = {-1:-1}
        ans = 0
        def getRepr(i):
            if uf[i]==i:
                return i
            else:
                uf[i] = getRepr(uf[i])
                return uf[i]
        
        for n in nums:
            if n not in uf:
                if n-1 in uf:
                    uf[n-1] = n
                if n+1 in uf:
                    uf[n]=n+1
                else:
                    uf[n]=n
            else:
                target = getRepr(n)
                v=target+1
                uf[target] = v
                ans += (v-n)
                if v+1 in uf:
                    uf[v]=v+1
                else:
                    uf[v]=v
        return ans