# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans=0
        def getdic(nd):
            if not nd:
                return {}
            if nd.left==None and nd.right==None:
                return {0:1}
            if nd.left==None or nd.right==None:
                d = getdic(nd.left or nd.right)
                return {(k+1):v for k,v in d.items() if k<distance}
            ld = getdic(nd.left)
            rd = getdic(nd.right)
            ldval = 0
            for dist in range(distance-1):
                ldval += ld.get(dist,0)
            for dist in range(distance-1):
                self.ans += ldval * rd.get(dist,0)
                ldval -= ld.get(distance-2-dist,0)
            nd = {}
            for k,v in ld.items():
                if k<distance:
                    nd[k+1] = nd.get(k+1,0)+v
            for k,v in rd.items():
                if k<distance:
                    nd[k+1] = nd.get(k+1,0)+v
            return nd
        getdic(root)
        return self.ans