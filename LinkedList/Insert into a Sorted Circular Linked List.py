"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node =  Node(insertVal)

        # Corner case
        if not head:
            new_node.next = new_node
            return new_node

        prev, cur = head, head.next

        # Look for the insertion condition.
        # break the while loop once found the place to insert
        while prev.next != head: # stop to insert new_node between prev and cur
            # Case1: 1 <- Node(2) <- 3
            if prev.val <= new_node.val <= cur.val:
                break

            # Case2: 3 -> 1, 3 -> Node(4) -> 1, 3 -> Node(0) -> 1
            #   prev is the last node of the list: prev.val > cur.val
            #   Add new_node between prev and cur when
            #       1) new_node is the new biggest node: new_node.val > prev.val
            #       2) new_node is the smallest node: new_node.val < cur.val
            if prev.val > cur.val and (new_node.val > prev.val or new_node.val < cur.val):
                break

            prev, cur = prev.next, cur.next

        # Insert node.
        # Case 4: [3, 3, 3] & new_node == 3 as well.
        new_node.next = cur
        prev.next = new_node

        return head
