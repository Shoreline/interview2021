# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Merge sort
# recursively call below steps, untill the list has only 0 or 1 node
# 1) find the middle node
# 2) break the linked list into two lists at the middle node. (middle node goes with the former list)
# 3) sort each list separately
# 4) merge
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):  # stop when list is empy or only has one node
            return head

        mid_node = self.findMiddle(head)
        head2 = mid_node.next  # head of the 2nd half
        mid_node.next = None  # separate the 1st and 2nd half list

        return self.merge(self.sortList(head), self.sortList(head2))

    def findMiddle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # easy to get wrong, can't just use the code from cycle I&II

    # ver3
    # def findMiddle(self, head: ListNode) -> ListNode:
    #     if not (head and head.next):
    #         return head
    #     if not head.next.next:
    #         return head
    #     walker = head
    #     runner = head
    #     while runner and runner.next:
    #         walker = walker.next
    #         runner = runner.next.next
    #     return walker

    # ver2
    # def findMiddle(self, head: ListNode) -> ListNode:
    #     if not (head and head.next):
    #         return head
    #     walker = head
    #     runner = head
    #     while runner and runner.next and runner.next.next: # !!!
    #         walker = walker.next
    #         runner = runner.next.next
    #     return walker

    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        pre_head = ListNode()
        tail = pre_head

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        tail.next = head1 if head1 else head2
        return pre_head.next