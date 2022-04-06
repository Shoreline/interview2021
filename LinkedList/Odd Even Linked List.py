# Build two lists, odd and even; then glue them together
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = head
        even = ListNode()  # dummy node
        even_head = head.next

        cur = head.next
        i = 2
        while cur:
            if i % 2 == 1:
                odd.next = cur

                cur = cur.next
                odd = odd.next
                odd.next = None
            else:
                even.next = cur

                cur = cur.next
                even = even.next
                even.next = None

            i += 1

        odd.next = even_head  # head next is always the head of the even list

        return head



