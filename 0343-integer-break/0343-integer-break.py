class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        if n==4:
            return 4
        t=n//3
        r=n%3
        if r==1:
            return 3**(t-1) * 4
        elif r==2:
            return 3**t*2
        return 3**t

        