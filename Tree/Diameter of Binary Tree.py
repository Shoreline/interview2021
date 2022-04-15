# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Find the longest path between any two nodes in a tree.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # returns the maximum depth starting from the input node
        def helper(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)

            # 1 + left/right: use node's ascendant as part of the path
            # 1 + left + right: don't use node's ascendant as part of the path
            res = max(res, 1 + left, 1 + right, 1 + left + right)

            return 1 + max(left, right)

        res = 0
        helper(root)
        return res - 1  # -1 since res is the number of nodes.

# class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         ans = [0]
#         self.helper(root, 0, ans)
#         return ans[0] - 1

#     def helper(self, node: TreeNode, curMax: int, ans: List[int]) -> int:
#         if not node:
#             return curMax

#         left = self.helper(node.left, curMax, ans)
#         right = self.helper(node.right, curMax, ans)

#         # if use node's ascendant as part of the path
#         len1 = curMax + 1 + max(left, right)
#         # if not to use node' ascendant as part of the path
#         len2 =  1 + left + right

#         ans[0] = max(ans[0], len1, len2)

#         return len1
