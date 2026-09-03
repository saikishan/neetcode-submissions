# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return

        p = head
        q = head.next
        p.next = None

        while(q):
            r = q.next
            q.next = p
            p, q = q, r

        return p
