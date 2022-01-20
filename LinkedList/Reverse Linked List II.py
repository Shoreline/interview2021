# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # find the start node
        pre_head = ListNode()
        pre_head.next = head
        seg_pre = pre_head
        i = 1  # left/right are 1-indexed
        while i < left:
            seg_pre = seg_pre.next
            i += 1

        pre = seg_pre
        cur = pre.next
        while i < right + 1:  # right is inclusive!
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            i += 1

        # At this moment, pre is the last node in segment, and cur is the first node outside the segment
        # seg_pre.next still points the original first node in segment (which is the seg tail node now)
        seg_pre.next.next = cur
        seg_pre.next = pre

        return pre_head.next
