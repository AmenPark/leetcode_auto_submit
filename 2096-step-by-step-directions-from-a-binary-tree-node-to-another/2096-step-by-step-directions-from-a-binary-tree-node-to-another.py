# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        result={}
        def to_find(node, tgs, path=[]):
            if len(result)==2:
                return
            if not node:
                return
            if node.val in tgs:
                result[node.val]=path[:]
            path.append("L")
            to_find(node.left, tgs, path)
            path[-1]="R"
            to_find(node.right,tgs,path)
            path.pop()
        to_find(root, [startValue, destValue])
        p1 = result[startValue]
        p2=result[destValue]
        print(p1,p2)
        ans=""
        i=0
        for i, (ch1,ch2) in enumerate(zip(p1,p2)):
            if ch1==ch2:
                continue
            break
        ans="U"*(len(p1)-i)
        ans+="".join(p2[i:])
        return ans
        