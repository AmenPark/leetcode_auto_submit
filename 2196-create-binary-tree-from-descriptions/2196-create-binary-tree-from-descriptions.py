# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nd={}
        checked=set()
        root=set()
        for p,c,l in descriptions:
            checked.add(c)
            root.discard(c)
            if p not in checked:
                root.add(p)
            pnd = nd.get(p,TreeNode(p))
            cnd = nd.get(c,TreeNode(c))
            if l:
                pnd.left=cnd
            else:
                pnd.right=cnd
            nd[p]=pnd
            nd[c]=cnd
        r=root.pop()
        return nd[r]