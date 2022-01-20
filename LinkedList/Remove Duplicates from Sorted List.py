# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val != cur.next.val:
                cur = cur.next
            else:
                # can't advance cur yet: the next next element may still be the same as cur
                cur.next = cur.next.next
        return head

# Two pointers. Maintain ptr1 as the tail (ptr1.next = None) and keep attaching nodes to the tail.
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None

#         ptr1, ptr2 = head, head.next
#         head.next = None

#         while ptr2:
#             if ptr1.val == ptr2.val:
#                 ptr2 = ptr2.next
#             else:
#                 ptr1.next = ptr2
#                 ptr1 = ptr1.next
#                 ptr2 = ptr2.next
#                 ptr1.next = None


#         return head