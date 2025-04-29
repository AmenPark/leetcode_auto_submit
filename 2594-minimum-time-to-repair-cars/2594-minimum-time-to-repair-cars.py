class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def getCars(time):
            rt = 0
            for rk in ranks:
                rt += int(sqrt(time/rk))
            return rt
        r=1
        while (w:=getCars(r))<cars:
            r<<=1

        l=r>>1
        while l<r-1:
            m=(l+r)//2
            if getCars(m)<cars:
                l=m
            else:
                r=m
        return r