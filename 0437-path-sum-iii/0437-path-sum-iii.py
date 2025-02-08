# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans=0
        ct={0:1}
        def pathSearch(nd, nowsum):
            if not nd:
                return
            nowval = nowsum + nd.val
            self.ans += ct.get(nowval - targetSum,0)
            ct[nowval] = ct.get(nowval,0)+1
            pathSearch(nd.left,nowval)
            pathSearch(nd.right,nowval)
            ct[nowval] -= 1
            if ct[nowval]==0:
                del ct[nowval]
        
        pathSearch(root,0)
        return self.ans