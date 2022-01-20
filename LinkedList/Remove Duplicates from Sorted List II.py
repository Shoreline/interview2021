# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Let pre be the node before each segment
# Each segment is a continous set of duplicated nodes
# If segment length is > 1, skip the whole segment.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode()
        pre_head.next = head

        pre = pre_head
        cur = head
        count = 0

        while cur:
            if cur.val == pre.next.val:
                count += 1
            else:
                if count > 1:
                    pre.next = cur
                else:
                    pre = pre.next
                count = 1

            cur = cur.next

        if count > 1:
            pre.next = None

        return pre_head.next  # Don't return head, since head may also be removed

