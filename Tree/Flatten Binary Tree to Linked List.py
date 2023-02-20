# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Similar to iterative way to do pre-order traverse.
# This time, instead of simply appending cur node's value to a list,
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre_head = TreeNode()
        tail = pre_head
        stack = []
        while root or stack:
            if not root:
                root = stack.pop()

            # Processing part 1.
            # For traverse, the only processing is to add root.val to res[]. But this time things are more complicated.
            tail.right = root

            # Moving the pointer.
            if root.right:
                stack.append(root.right)
            root = root.left

            # Processing part 2
            tail.left = None
            tail = tail.right

        return pre_head.right

# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#
#         # flatten the subtree rooted at root, and return the rightmost node (so we can use the rightmost node to
#         # connect the other subtree)
#         def helper(root: TreeNode) -> TreeNode:
#             if not root:
#                 return None
#             elif not (root.left or root.right):  # if both left and right are none (root is a leaf node)
#                 return root
#
#             left_rightmost = helper(root.left)  # rightmost node of the left subtree
#             right_rightmost = helper(root.right)
#
#             if left_rightmost:  # if left subtree exists, move it to between root and root.right
#                 left_rightmost.right = root.right
#                 root.right = root.left
#
#             root.left = None
#             if right_rightmost:
#                 return right_rightmost
#             else:
#                 return left_rightmost
#
#         helper(root)

# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         return self.flattenHelper(root, [])

#     def flattenHelper(self, root: TreeNode, parent_node: List[TreeNode]) -> None:
#         if not root:
#             return

#         if not parent_node:
#             parent_node.append(root)
#         else:
#             parent_node[0].right = root

#         parent_node[0] = root # current root becomes the new parent
#         left, right = root.left, root.right # cache

#         self.flattenHelper(left, parent_node)
#         self.flattenHelper(right, parent_node)
#         root.left = None
#         return

