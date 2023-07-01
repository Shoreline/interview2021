# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # returns the height and the lca of the deepest leaves for a given root
        def helper(root):
            if not root:
                return 0, None

            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)

            if h1 > h2:  # left is deeper
                return h1 + 1, lca1
            elif h1 < h2:
                return h2 + 1, lca2
            else:
                return h1 + 1, root

        return helper(root)[1]