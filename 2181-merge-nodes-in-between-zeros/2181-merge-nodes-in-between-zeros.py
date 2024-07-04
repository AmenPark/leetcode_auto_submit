# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nd=head.next
        v=0
        head=ListNode()
        cur=head
        while nd:
            if nd.val:
                v+=nd.val
            else:
                cur.next=ListNode(v)
                cur=cur.next
                v=0
            nd=nd.next
        return head.next