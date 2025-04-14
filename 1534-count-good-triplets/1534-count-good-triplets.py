class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N=len(arr)
        ans=0
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[k]-arr[i])<=c:
                        ans+=1
        return ans