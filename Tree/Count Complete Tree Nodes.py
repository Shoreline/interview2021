# We are told that the given tree is complete.
# Compare the depth between left subtree and right subtree.
#   - Here the leftmost node is always the deepest node (nature of complete tree).
# A, If it is equal, it means the left subtree is a perfect binary tree
# B, If it is not equal, it means the left subtree is 1-level deeper, and the right subtree is a perfect binary tree
#
# O(log(n) * log(n))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # find the depth of a complete tree
        def findDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + findDepth(root.left)

        left_depth = findDepth(root.left)
        right_depth = findDepth(root.right)

        if left_depth == right_depth:
            # It is actually 1 (root) + [2^left_depth - 1] (left sub tree) + count(right sub tree)
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            return pow(2, right_depth) + self.countNodes(root.left)
