# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST helps us trim search by half
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            root = root.left if target < root.val else root.right
        return res


# class Solution:
#     def closestValue(self, root: Optional[TreeNode], target: float) -> int:
#         res = root.val
#         while root:
#             if root.val == target:
#                 return root.val
#             if abs(root.val - target) < abs(res - target):
#                 res = root.val
#
#             # Not necessary
#             # In BST, the smaller value node is always checked before a larger value node (right subtree)
#             # elif abs(root.val - target) == abs(res - target):
#             #     res = min(res, root.val)
#
#             if target < root.val:
#                 root = root.left
#             else:
#                 root = root.right
#         return res

# Not optimal, didn't utilize binary search tree
# class Solution:
#     def closestValue(self, root: Optional[TreeNode], target: float) -> int:
#         if not root:
#             return float('inf')

#         left = self.closestValue(root.left, target)
#         right = self.closestValue(root.right, target)

#         return sorted([left, right, root.val], key=lambda x: abs(x - target))[0]

