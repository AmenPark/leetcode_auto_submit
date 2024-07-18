# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        del_set=set(to_delete)
        ans = []
        def delnd(nd, isroot):
            if not nd:
                return True
            if nd.val in to_delete:
                delnd(nd.left, True)
                delnd(nd.right, True)
                return False
            if isroot:
                ans.append(nd)
            if not delnd(nd.left,False):
                nd.left=None
            if not delnd(nd.right,False):
                nd.right=None
            return True
        delnd(root,True)
        return ans