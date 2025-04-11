class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans=0
        for n in range(low,high+1):
            i=str(n)
            if len(i)%2==1:
                continue
            l=len(i)//2
            left = n//(10**l)
            right=n%(10**l)
            if sum(map(int, list(str(left))))==sum(map(int,list(str(right)))):
                ans+=1
        return ans
