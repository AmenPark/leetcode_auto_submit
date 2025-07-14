# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        nd=head
        ans=0
        while nd:
            ans<<=1
            ans+=nd.val
            nd=nd.next
        return ans