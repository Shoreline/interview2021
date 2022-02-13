# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# If there is a cycle. Then after the first meet, move runner back to starting node, and slow it down to have the same pace of walker
# Then the 2nd meeting of runner and walker will be at the entrance node of that cycle.
class Solution:  # wrong
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or (not head.next):  # corner case: if there is only one node, no cycle as well
            return None

        # walker and runner shall start on the same node!
        walker = head
        runner = head

        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                break

        if walker != runner:
            return None

        runner = head
        while runner != walker:
            walker = walker.next
            runner = runner.next

        return walker
