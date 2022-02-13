"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# No need to use prehead
# 1) Clone each node and insert the new node between original nodes in the list
# 2) go back to head, replicate random pointer
# 3) cut the cloned nodes out of the original list
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            new_node = Node(cur.val)
            #new_node.val = cur.val
            new_node.next = cur.next
            cur.next = new_node

            cur = new_node.next

        cur = head
        while cur:
            new_node = cur.next
            if cur.random: # easy to miss this check
                new_node.random = cur.random.next

            cur = cur.next.next

        new_head = head.next
        cur = new_head
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next

        return new_head

# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head:
#             return head

#         cur = head
#         while cur:  # "cur.next" is a wrong condition!
#             clone = Node(cur.val, cur.next)
#             cur.next = clone  # clone.next is already the next node of cur in original list
#             cur = clone.next

#         original = head
#         cloned = original.next
#         while original:
#             if original.random != None:
#                 cloned.random = original.random.next
#             original = original.next.next
#             if original:
#                 cloned = original.next
#             # if cloned.next != None:
#             #     cloned = cloned.next.next

#         original = head
#         cloned = original.next
#         cloned_head = cloned
#         while original:
#             original.next = cloned.next
#             if cloned.next != None:
#                 cloned.next = cloned.next.next

#             original = original.next
#             if original != None:
#                 cloned = original.next

#         return cloned_head
