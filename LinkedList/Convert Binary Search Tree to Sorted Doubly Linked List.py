"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


# in-order traversal
# Use a stack to save parent nodes for in-order traverse
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        pre_head = Node(-1)
        pre = pre_head
        cur = root
        stack = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            # link pre and cur as doubly-linked list
            cur = stack.pop()
            pre.right = cur
            cur.left = pre

            # advance pre and cur
            pre = cur
            cur = cur.right  # cur.right can be null, if so cur will be stack.pop() next round

        # In the end, finish circular linking
        pre_head.right.left = pre  # now pre is the last element. (cur is already None)
        pre.right = pre_head.right

        return pre_head.right
