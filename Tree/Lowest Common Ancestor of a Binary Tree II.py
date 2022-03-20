# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Note that p and q may NOT exist in the tree
# Key: keep traversing before returnning anything
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root:
                return None

            # keep traversing no matter if root is either p or q
            left = helper(root.left)
            right = helper(root.right)

            if root.val == p.val or root.val == q.val:
                self.count += 1
                return root

            if left and right:
                return root

            return left if left else right

        self.count = 0
        res = helper(root)
        return res if self.count == 2 else None

