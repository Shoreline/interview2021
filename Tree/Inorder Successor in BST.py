# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BST!!
# Finding condition of P: if a node > p, and all of its left subtree < p, then this node is the result
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)

        left = self.inorderSuccessor(root.left, p)
        return left if left else root

# class Solution:
#     def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
#         if not root:
#             return None
#
#         if root.val > p.val:
#             return self.inorderSuccessor(root.left, p) or root
#
#         return self.inorderSuccessor(root.right, p)

# For non-BST
# class Solution:
#     def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
#         pre_node = None
#         res = None
#
#         def inorder(root):
#             nonlocal pre_node
#             nonlocal res
#             if not root:
#                 return
#
#             inorder(root.left)
#             if not res and pre_node and pre_node.val == p.val:
#                 res = root
#                 return
#             pre_node = root
#             inorder(root.right)
#
#         inorder(root)
#         return res