# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heapList = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heapList, (lists[i].val, i, lists[i]))
        dummy = ListNode(0)
        tail = dummy

        while len(heapList):
            val, i, leastNode = heapq.heappop(heapList)
            tail.next = leastNode
            tail = leastNode
            if leastNode.next:
                heapq.heappush(heapList, (leastNode.next.val, i, leastNode.next))

        return dummy.next
