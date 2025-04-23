# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ls = [root]
        depth = 0
        while ls[0].left:
            nls = []
            for nd in ls:
                nls.append(nd.left)
                nls.append(nd.right)
            if depth%2==0:
                M=len(nls)
                for i in range(M//2):
                    nls[i].val, nls[M-1-i].val = nls[M-1-i].val, nls[i].val
            ls = nls
            depth+=1
        return root