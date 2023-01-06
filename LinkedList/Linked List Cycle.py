# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Let walker and runner start from the same node!
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        walker = head
        runner = head

        # When there is a cycle, this condition will always be true
        while walker and runner and runner.next:
            walker = walker.next
            runner = runner.next.next

            if walker and runner and walker == runner:
                return True

        return False

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if not (head and head.next):
#             return None
#
#         walker = head
#         runner = head
#
#         while runner and runner.next:
#             walker = walker.next
#             runner = runner.next.next
#             if walker == runner:
#                 return True
#
#         return False

# Below works for this problem, but doesn't work for cycle II, since walker and runner do not start from the same node.
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if not head or (not head.next):
#             return False

#         walker = head
#         runner = head.next

#         while walker!=runner and runner and runner.next:
#             walker = walker.next
#             runner = runner.next.next

#         return True if walker == runner else False


