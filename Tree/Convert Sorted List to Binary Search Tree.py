# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The requirement is not a random BST, but a height-balanced binary search tree.
# Inorder simulation
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def inorder(start: int, end: int) -> TreeNode:
            if start > end:
                return None

            mid = start + (end - start) // 2
            left = inorder(start, mid - 1)
            root = TreeNode(self.pos.val)
            self.pos = self.pos.next
            root.left = left
            root.right = inorder(mid + 1, end)

            return root

        self.pos = head
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        return inorder(0, count - 1)