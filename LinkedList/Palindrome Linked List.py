# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# /*
#  * Time:O(N); Space: O(1).
#  *
#  * Thought: find middle node, cut the list into two half, reverse one of
#  * them, then compare values
#  *
#  * *Even if there is odd number of nodes in original list, the middle node
#  * later become the last node of the reversed second half. It will not be
#  * compared. So it is fine to ignore it.
#  */
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        pre_head = ListNode()
        pre_head.next = head
        walker, runner = pre_head, pre_head
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next

        cur = walker.next
        next = cur.next
        walker.next = None
        while cur and next:
            tmp = next.next
            next.next = cur
            cur = next
            next = tmp

        while head and cur:
            if head.val != cur.val:
                return False
            head = head.next
            cur = cur.next
            print(3)

        return True


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        # Measure the list length
        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next

        # find the middle node
        cur = head
        for i in range(list_len // 2):
            cur = cur.next

        mid = cur

        pre = None
        cur = head
        while cur and cur != mid:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        cur = pre
        if list_len % 2 == 1:
            mid = mid.next
        while cur:
            if cur.val == mid.val:
                cur = cur.next
                mid = mid.next
            else:
                return False

        return True        