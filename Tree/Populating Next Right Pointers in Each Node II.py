"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Level traverse.
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1: # Only the last node in this level don't have next pointing to anyone.
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


# Node is the pointer in the parent level, cur is the tail pointer in the child level.
# The parent level can be view as a singly linked list or queue, which we can traversal easily with a pointer.
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         node = root
#         while node:
#             # lvl_preHead is a helper variable used to point to leftmost node in the next level
#             lvl_preHead = Node()
#             cur = lvl_preHead
#             #cur = lvl_preHead = Node(0) equivalent
#             while node:
#                 if node.left:
#                     cur.next = node.left
#                     cur = cur.next
#                 if node.right:
#                     cur.next = node.right
#                     cur = cur.next
#                 node = node.next
#             node = lvl_preHead.next # lvl_preHead has been assigned to the leftmost node when lvl_preHead == cur
#         return root
