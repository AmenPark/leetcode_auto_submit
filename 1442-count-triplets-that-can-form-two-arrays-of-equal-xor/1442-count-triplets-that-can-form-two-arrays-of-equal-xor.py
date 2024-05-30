class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        d = {0:(1,-1,1)}
        v=0
        ans=0
        for t,x in enumerate(arr):
            v^=x
            a,b,c = d.get(v,(0,0,0))
            ans += a+(t-b-2)*c
            d[v] = (a+(t-b)*c+1,t,c+1)
        return ans