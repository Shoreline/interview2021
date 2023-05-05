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

        odd_tail = head # odd_head is fixed to be the head itself.
        EVEN_HEAD = head.next  # constant, always the head of the even list
        even_tail = ListNode()  # dummy node, also the prehead of the even list

        cur = head.next
        i = 2
        while cur:
            if i % 2 == 1:
                odd_tail.next = cur

                cur = cur.next
                odd_tail = odd_tail.next
                odd_tail.next = None
            else:
                even_tail.next = cur

                cur = cur.next
                even_tail = even_tail.next
                even_tail.next = None

            i += 1

        odd_tail.next = EVEN_HEAD  # head next is always the head of the even list

        return head



