# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This time, find the LCA of not just two, but a set of nodes. (set size can be just 1)
# "All the nodes will exist in the tree" !!! So we can still return root as long as root is one of the node in node set.
# All Node.val are unique
# All nodes[i] are distinct.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        node_set = set(nodes)

        def helper(root: 'TreeNode') -> 'TreeNode':
            if not root:
                return None
            if root in node_set:
                return root

            left = helper(root.left)
            right = helper(root.right)

            if left and right:
                return root
            return left if left else right

        return helper(root)