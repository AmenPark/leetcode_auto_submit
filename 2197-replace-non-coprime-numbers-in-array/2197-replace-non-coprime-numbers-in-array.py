class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        def gcd(x,y):
            if x%y==0:
                return y
            return gcd(y,x%y)
        for n in nums:
            if not ans:
                ans.append(n)
                continue
            gcdval=gcd(n,ans[-1])
            nval=n
            while gcdval>1:
                nval *= ans.pop()//gcdval
                if not ans:
                    break
                gcdval = gcd(nval,ans[-1])
            ans.append(nval)
        return ans