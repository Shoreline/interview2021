# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# All values are unique!
#
# Note that this solution does NOT assume p and q always exist in the tree
# Key: Traverse both subtrees before returning anything
#
# Time Complexity: O(N)
# Space Complexity: O(H), H is the height of the tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Returns one of the {LCA, p, q} node
        # We don't know what's returned (LCA, or simply just p or q) unless checking the self.count
        #
        # If root is p or q, returns root
        # If root is the answer (LCA of p/q), returns root
        # If any of the dependent node under root is p or q or LCA, returns that node
        def find_and_count(root):
            if not root:
                return None

            # Need to anyway traverse left and right subtrees
            left = find_and_count(root.left)
            right = find_and_count(root.right)

            if root == p or root == q:
                self.count += 1
                return root

            if left and right:
                return root

            return left if left else right

        self.count = 0
        res = find_and_count(root)
        if res and self.count == 2:
            return res
        else:
            return None

