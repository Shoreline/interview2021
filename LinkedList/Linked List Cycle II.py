# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# If there is a cycle. Then after the first meet, move runner back to starting node, and slow it down to have the same
# pace of walker. Then the 2nd meeting of runner and walker will be at the entrance node of that cycle.
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        walker, runner = head, head

        # First meet
        while walker and runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                break

        if not walker or not runner or not runner.next: # other conditions can hardly handle all corner cases.
            return None

        runner = head
        while runner != walker:
            walker = walker.next
            runner = runner.next

        return runner
