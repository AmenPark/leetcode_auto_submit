class Solution:
    def integerReplacement(self, n: int) -> int:
        ans=-1
        while n:
            ans+=1
            if n&1==0:
                n//=2
            elif n&3==3:
                if n==3:
                    n-=1
                    continue
                n+=1
            else:
                n-=1
        return ans