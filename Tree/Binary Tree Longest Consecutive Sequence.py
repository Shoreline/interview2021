# A consecutive sequence path is a path where the values increase by one along the path.

# Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_iterative:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        stack = [(root, 1)]
        while stack:
            node, cnt = stack.pop()

            for child in [node.left, node.right]:
                if not child:
                    continue
                if child.val == node.val + 1:
                    stack.append((child, cnt + 1))
                else:
                    stack.append((child, 1))

            res = max(res, cnt)

        return res


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def longest_path(root):
            if not root:
                return 0
            length = 1
            l = longest_path(root.left)
            r = longest_path(root.right)
            if root.left and root.left.val == root.val + 1:
                length = max(length, 1 + l)
            if root.right and root.right.val == root.val + 1:
                length = max(length, 1 + r)
            res[0] = max(res[0], length)
            return length

        res = [0]
        longest_path(root)
        return res[0]
