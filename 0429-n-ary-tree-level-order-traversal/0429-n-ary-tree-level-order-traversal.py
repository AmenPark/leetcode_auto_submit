"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        def getT(nd, depth):
            if len(ans)==depth:
                ans.append([])
            ans[depth].append(nd.val)
            for nnd in nd.children:
                getT(nnd, depth+1)
        if root:
            getT(root,0)
        return ans