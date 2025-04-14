class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N=len(arr)
        ans=0
        for i in range(N):
            for j in range(i+1,N):
                if abs(arr[i]-arr[j])>a:
                    continue
                m=max(arr[i]-c, arr[j]-b)
                M=min(arr[i]+c, arr[j]+b)
                for k in range(j+1,N):
                    if m<=arr[k]<=M:
                        ans+=1
        return ans