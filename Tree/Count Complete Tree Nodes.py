# Compare the depth between left sub tree and right sub tree.
# A, If it is equal, it means the left sub tree is a perfect  binary tree
# B, It it is not, it means the right sub tree is a perfect  binary tree
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

        # find the depth of a tree
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
            return self.countNodes(root.left) + pow(2, right_depth)
