# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def findorder(root,l):
                if not root:
                    return
                findorder(root.left,l)
                l.append(root.val)
                findorder(root.right,l)
        l = []
        findorder(root,l)
        def create_tree(l,i,j):
            if i>j:
                return None
            if i==j:
                return TreeNode(l[i])
            mid = (i+j)//2
            left = create_tree(l,i,mid-1)
            right=create_tree(l,mid+1,j)
            return TreeNode(l[mid], left, right)
            
        return create_tree(l,0,len(l)-1)