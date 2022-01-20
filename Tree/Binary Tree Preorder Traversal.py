# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         def helper(root:TreeNode):
#             if root:
#                 res.append(root.val)
#                 helper(root.left)
#                 helper(root.right)

#         res = []
#         helper(root)
#         return res

# Iteration
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]

        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)

                # First push the node you want to pop later
                stack.append(root.right)
                stack.append(root.left)

        return res

# Moris traversal
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         node, output = root, []
#         while node:
#             if not node.left:
#                 output.append(node.val)
#                 node = node.right
#             else: 
#                 predecessor = node.left

#                 while predecessor.right and predecessor.right is not node:
#                     predecessor = predecessor.right

#                 if not predecessor.right:
#                     output.append(node.val)
#                     predecessor.right = node
#                     node = node.left
#                 else:
#                     predecessor.right = None
#                     node = node.right

#         return output