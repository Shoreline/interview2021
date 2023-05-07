# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import queue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pre_head = tail = ListNode(0)

        pq = queue.PriorityQueue()

        for idx, node in enumerate(lists):
            if node:
                pq.put((node.val, idx, node))

        while not pq.empty():
            _, idx, node = pq.get()
            if node.next:
                pq.put((node.next.val, idx, node.next))
            tail.next = node
            tail = tail.next

        return pre_head.next

# class ListNodeExtension(ListNode):
#     def __lt__(self, other):
#         return self.val < other.val
#
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         ListNode.__lt__ = ListNodeExtension.__lt__
#         heap = []
#
#         # Push head nodes of all lists into heap
#         for n in lists:
#             if n:
#                 heapq.heappush(heap, n)
#
#         pre_head = tail = ListNode(0)  # Result pointers
#         while heap:
#             tail.next = heapq.heappop(heap)
#             tail = tail.next
#             if tail.next:
#                 heapq.heappush(heap, tail.next)
#
#         return pre_head.next