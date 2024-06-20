class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l=0
        r=position[-1]
        def check(gap):
            bp = position[0] - gap
            ct=0
            for p in position:
                if p-bp>=gap:
                    ct+=1
                    bp=p
            return ct
        while l<r-1:
            mm=(l+r)//2
            ct=check(mm)
            if ct>=m:
                l=mm
            else:
                r=mm
        return l
