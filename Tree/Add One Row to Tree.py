# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root or depth <= 0 :
            return None

        if depth == 1: # Problem statement says to simply add root as the left node of the new node.
            return TreeNode(val, root, None)
        if depth == 2: # The most common case
            # add a new tree node, and attach root.left to be the left tree of this new node
            root.left = TreeNode(val, root.left, None)
            # add a new tree node, and attach root.right to be the right tree of this new node
            root.right = TreeNode(val, None, root.right)
        else:
            root.left == self.addOneRow(root.left, val, depth - 1)
            root.right == self.addOneRow(root.right, val, depth - 1)
        return root