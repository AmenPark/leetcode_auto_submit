# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        ans = []
        while q:
            mv = -float("inf")
            nq = []
            for nd in q:
                mv=max(mv,nd.val)
                if nd.left:
                    nq.append(nd.left)
                if nd.right:
                    nq.append(nd.right)
            ans.append(mv)
            q=nq
        return ans