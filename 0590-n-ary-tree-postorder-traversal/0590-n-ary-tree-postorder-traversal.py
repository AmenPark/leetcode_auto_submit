"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        st1=[]
        st2=[]
        ans=[]
        cur=root
        if not root:
            return []
        pt=0
        while True:
            if cur.children==None:
                ans.append(cur.val)
                if not st1:
                    return ans
                cur = st1.pop()
                pt=st2.pop()
            elif len(cur.children)==pt:
                ans.append(cur.val)
                if not st1:
                    return ans
                cur=st1.pop()
                pt=st2.pop()
            else:
                st1.append(cur)
                st2.append(pt+1)
                cur=cur.children[pt]
                pt=0
        

            
