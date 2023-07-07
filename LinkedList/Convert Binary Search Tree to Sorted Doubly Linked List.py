"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
# in-order traversal
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return

        dummy = Node(0, None, None) # serves as preHead
        pre = dummy
        stack = []
        cur = root # current node
        while stack or cur:
            if cur:
               stack.append(cur)
               cur = cur.left
            else:
                cur = stack.pop()
                pre.right = cur
                cur.left = pre

                pre = pre.right
                cur = cur.right

        # In the end, finish circular linking
        dummy.right.left = pre # now pre is the last element. (cur is already None)
        pre.right = dummy.right

        return dummy.right

class Solution2:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return

        dummy = Node(0, None, None) # serves as preHead
        pre = dummy
        stack = []
        cur = root # current node
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            # link pre and cur as doulbly-linked list
            pre.right = cur
            cur.left= pre

            # advance pre and cur
            pre = cur # or per = pre.right
            cur = cur.right # cur.right can be null, if so cur will be stack.pop() next round

        # In the end, finish circular linking
        dummy.right.left = pre # now pre is the last element. (cur is already None)
        pre.right = dummy.right

        return dummy.right
