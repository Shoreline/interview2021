# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Need to reverse a specified segment.
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # find the start node
        pre_head = ListNode()
        pre_head.next = head
        seg_pre = pre_head
        # left/right are 1-indexed
        for i in range(left - 1): # left - 1 to reach one node before left
            seg_pre = seg_pre.next

        pre = seg_pre
        cur = pre.next
        for i in range(left, right+1):  # Need nodes in [left, right] (right is inclusive)
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        # At this moment, pre is the last node in segment, and cur is the first node outside the segment
        # seg_pre.next still points the original first node in segment (which is the seg tail node now)
        seg_pre.next.next = cur
        seg_pre.next = pre

        return pre_head.next
