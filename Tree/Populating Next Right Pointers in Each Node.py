"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# /*
#  * This method only good for this question. It assumes that the binary tree
#  * is perfect
#  *
#  * For each node, connect
#       1) root.left.next = root.right
#       2) root.right.next = root.next.left
#  */
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        if root.left:
            root.left.next = root.right

        if root.right and root.next:  # For the right node, taking advantage of root.next
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
