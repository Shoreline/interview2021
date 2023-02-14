# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The helper function does two things
#   1) computes the maximum path sum of root's subtrees (either left or right subtree);
#   2) returns the maximum sum if "using node as part of the path sum of super-tree that includes the sub-tree rooting
#      on node
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')

        # Returns the maximum path sum starting at root
        # - If path is not empty, root must be included in this path.
        # - Or, path is empty, then the path sum is 0.
        def helper(root: TreeNode) -> int:
            if not root:
                return 0

            leftmax = helper(root.left)
            rightmax = helper(root.right)

            self.res = max(self.res, root.val + leftmax + rightmax)

            # 0 means don't take any subtree of root as part of the path (since the sum is negative)
            return max(0, root.val + max(leftmax, rightmax))

        helper(root)
        return self.res

# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         tmp_max = [-sys.maxsize]
#         self.helper(root, tmp_max)
#         return tmp_max[0]

#     def helper(self, node: TreeNode, tmp_max: List[int]) -> int:
#         if not node:
#             return 0

#         left_max = self.helper(node.left, tmp_max)
#         right_max = self.helper(node.right, tmp_max)
#         tmp_max[0] = max(tmp_max[0], node.val + max(0, left_max) + max(0, right_max))

#         return node.val + max(0, left_max, right_max)


# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         tmp_max = [-sys.maxsize]
#         self.helper(root, tmp_max)
#         return tmp_max[0]

#     def helper(self, node: TreeNode, tmp_max: List[int]) -> int:
#         if not node:
#             return 0

#         left_max = self.helper(node.left, tmp_max)
#         right_max = self.helper(node.right, tmp_max)
#         #sub_tree_max = node.val

#         tmp_max[0] = max(tmp_max[0], node.val + max(0, left_max) + max(0, right_max))

#         if left_max < 0 and right_max < 0:
#             return node.val
#         else:
#             return node.val + max(left_max, right_max)
