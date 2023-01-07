# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Let pre be the node before each segment.
# Each segment is a continuous set of duplicated nodes
# If segment length is > 1, skip the whole segment.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode()
        pre_head.next = head

        pre = pre_head
        cur = head
        count = 0

        while cur:
            if cur.val == pre.next.val:  # segment continues
                count += 1
            else:  # segment ends
                if count > 1:
                    pre.next = cur  # skip the whole segment
                else:
                    pre = pre.next  # Found a distinct element, move forward.
                count = 1

            cur = cur.next

        if count > 1:
            pre.next = None

        # Don't return head, since head may also be removed
        return pre_head.next
