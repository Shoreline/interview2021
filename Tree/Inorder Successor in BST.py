# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BST!!
# Finding condition of P: if a node > p, and all of its left subtree < p, then this node is the result
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val > p.val:
            return self.inorderSuccessor(root.left, p) or root

        return self.inorderSuccessor(root.right, p)