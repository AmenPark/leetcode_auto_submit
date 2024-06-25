# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        hq=[]
        def getsum(nd):
            if not nd:
                return 0
            heapq.heappush(hq,(nd.val,nd))
            return getsum(nd.left)+getsum(nd.right)+nd.val
        ss=getsum(root)
        while hq:
            v,nd=heapq.heappop(hq)
            ss-=v
            nd.val+=ss
        return root