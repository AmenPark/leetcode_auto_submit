# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        bnd=head
        nd=bnd.next
        if nd.next==None:
            return [-1,-1]
        nnd=nd.next
        while nnd:
            if bnd.val<nd.val and nd.val>nnd.val:
                break
            if bnd.val>nd.val and nd.val<nnd.val:
                break
            bnd=nd
            nd=nnd
            nnd=nnd.next
        
        maxval=-1
        minval=10000000
        cid=0
        nid=1
        bnd=nd
        nd=nnd
        nnd=nnd.next
        while nnd:
            if (bnd.val<nd.val and nd.val>nnd.val) or(bnd.val>nd.val and nd.val<nnd.val):
                maxval=nid
                minval=min(minval, nid-cid)
                print(nid)
                cid=nid
            bnd=nd
            nd=nnd
            nnd=nnd.next
            nid+=1
        if maxval==-1:
            return [-1,-1]
        return [minval, maxval]

            