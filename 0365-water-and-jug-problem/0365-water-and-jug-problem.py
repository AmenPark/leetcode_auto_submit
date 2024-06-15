class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x>y:
            x,y=y,x
        now = {(0,0)}
        recent = {(0,0)}
        while recent:
            nrecent = set()
            for a,b in recent:
                for ntg in [(x,b),(0,b),(a,y),(a,0),(x,b-(x-a)) if a+b>x else (a+b,0),(a-(y-b), y) if a+b>y else (0,a+b)]:
                    if ntg in now:
                        continue
                    if sum(ntg)==target:
                        return True
                    nrecent.add(ntg)
                    now.add(ntg)
            recent=nrecent
        return False