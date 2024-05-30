class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        s=[0]
        v=0
        for x in arr:
            v^=x
            s.append(v)
        N=len(s)
        ans=0
        for i in range(N-1):
            for j in range(i+1,N):
                if s[i]==s[j]:
                    ans+=(j-i-1)
        return ans