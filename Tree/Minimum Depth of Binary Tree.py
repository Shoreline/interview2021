# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# /*
#  * Be careful of the definition of minimum depth.
#  *
#  * If one of the children of root is null, then its min depth is 1 + min_depth
#  * of the other node (still true even if the other node is also null)
#  */

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 1 + self.minDepth(root.left) if root.left else 1 + self.minDepth(root.right)

# Wrong answer
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         return 1 + min(self.minDepth(root.left), self.minDepth(root.right))