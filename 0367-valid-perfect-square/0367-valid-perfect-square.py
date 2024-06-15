class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=1
        while r**2 < num:
            r<<=1
        if r**2 == num:
            return True
        while l<r-1:
            m=(l+r)//2
            if m**2 <num:
                l=m
            else:
                r=m
        if r**2==num:
            return True
        return False