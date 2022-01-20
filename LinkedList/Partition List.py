# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Simply build two separate lists and linked them together at the end.
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        pre_head = ListNode()
        pre_head2 = ListNode()

        cur = head
        tail1, tail2 = pre_head, pre_head2

        while cur:
            if cur.val < x:
                tail1.next = cur
                cur = cur.next
                tail1 = tail1.next
                tail1.next = None
            else:
                tail2.next = cur
                cur = cur.next
                tail2 = tail2.next
                tail2.next = None

        tail1.next = pre_head2.next
        return pre_head.next
