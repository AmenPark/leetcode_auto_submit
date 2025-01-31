class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        finder = []
        for x,y,a,b in rectangles:
            finder.append((y,x, 1))
            finder.append((y,a, -1))
            finder.append((b,x,-1))
            finder.append((b,a,1))
        finder.sort()
        l = [(-99999,-99999,0)]
        for a,b,c in finder:
            if l[-1]==(a,b,-c):
                l.pop()
            else:
                l.append((a,b,c))
        return len(l)==5