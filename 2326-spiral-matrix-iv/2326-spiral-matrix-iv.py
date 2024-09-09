# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        def directions():
            while True:
                yield (0,1)
                yield 1,0
                yield 0,-1
                yield -1,0
        gen = directions()
        x=0
        y=-1
        dir = next(gen)
        nd = head
        while nd:
            ndval=nd.val
            while True:
                dx,dy = dir
                if 0<=x+dx<m and 0<=y+dy<n and ans[x+dx][y+dy]==-1:
                    break
                dir=next(gen)
            x+=dx
            y+=dy
            ans[x][y] = ndval
            nd=nd.next

        return ans