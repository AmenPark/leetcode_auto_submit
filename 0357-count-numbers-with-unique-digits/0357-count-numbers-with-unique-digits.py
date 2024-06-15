class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        f=[1]
        for i in range(1,11):
            f.append(f[-1]*i)
        ans = 0
        c=[9]
        k=9
        for _ in range(n):
            ans += reduce(lambda x,y:x*y, c,1)
            c.append(k)
            k-=1
        return ans+1
