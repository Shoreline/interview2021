# Use a helper function to reverse a given LinkedList
# Identify every segment of k nodes and call that helper function.
# O(N) and O(1)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:  # must have. below code is wrong for k = 1 case.
            return head

        pre, cur = ListNode(-1), head
        pre.next = head

        # seg_pre: one node ahead of current segment
        # seg_head: first node of current segment
        seg_pre, seg_head = pre, cur
        count = 1

        while cur:
            next = cur.next

            if count % k == 1:  # cur is the first node of a new segment
                seg_head = cur
            elif count % k == 0:  # cur is the last node of a segment
                cur.next = None  # cut the end of this segment off from the main list so we can reverse this segment
                # After reversing, seg_head will become the last node of current segment
                seg_pre.next = self.reverseList(seg_head)
                seg_pre = seg_head  # reset seg_pre to be the last node of current segment -> one node ahead of next segment
                seg_pre.next = next

            cur = next
            count += 1

        return pre.next

    # reverse a LinkedList starting from head, and returns the new head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre