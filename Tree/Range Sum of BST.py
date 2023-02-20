# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Take advantage of the fact that the tree is a BST, can skip some part of the traverse.
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root):
            if not root:
                return

            if low <= root.val <= high:
                self.res += root.val
            if root.val > low:  # this is a binary search tree
                helper(root.left)
            if root.val < high:
                helper(root.right)

        self.res = 0
        helper(root)
        return self.res

# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         res = 0
#         def helper(root):
#             nonlocal res
#             if not root:
#                 return

#             if root.val >= low and root.val <= high:
#                 res += root.val
#             helper(root.left)
#             helper(root.right)

#         helper(root)
#         return res