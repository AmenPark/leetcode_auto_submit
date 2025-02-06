"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def createNode(grid, x1,y1,x2,y2):
            if x2-x1==1:
                return Node(grid[x1][y1], 1, None,None,None,None)
            mx = (x1+x2)//2
            my=(y1+y2)//2
            tl = createNode(grid, x1,y1,mx,my)
            tr = createNode(grid,x1,my,mx,y2)
            bl = createNode(grid,mx,y1,x2,my)
            br = createNode(grid,mx,my,x2,y2)
            vs = tl.val+tr.val+bl.val+br.val
            if vs==0:
                return Node(0,1,None,None,None,None)
            elif vs==4:
                return Node(1,1,None,None,None,None)
            else:
                return Node(1,0,tl,tr,bl,br)
        return createNode(grid,0,0,len(grid),len(grid))
            
        