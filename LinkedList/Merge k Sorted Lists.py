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
                pq.put((node.val, idx, node)) # idx is used as a tiebreaker.

        while not pq.empty():
            _, idx, node = pq.get()
            if node.next:
                pq.put((node.next.val, idx, node.next))
            tail.next = node
            tail = tail.next

        return pre_head.next


# Heap alternative 1: tiebreaker
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         heap = []
#         pre_head = tail = ListNode(0)
#         for i, head in enumerate(lists):
#             if head:
#                 heapq.heappush(heap, (head.val, i, head))


#         while heap:
#             _, i, node = heapq.heappop(heap)
#             tail.next = node
#             tail = tail.next
#             if node.next:
#                 heapq.heappush(heap, (node.next.val, i, node.next))

#         return pre_head.next

# Heap alternative 2: implement ListNode.__lt__ with lambda
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         ListNode.__lt__ = lambda self, other: self.val < other.val
#
#         heap = []
#         pre_head = tail = ListNode(0)
#         for head in lists:
#             if head:
#                 heapq.heappush(heap, head)
#
#         while heap:
#             node = heapq.heappop(heap)
#             tail.next = node
#             tail = tail.next
#             if node.next:
#                 heapq.heappush(heap, node.next)
#
#         return pre_head.next

# Heap alternative 3: implement ListNode.__lt__ with a separate class
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