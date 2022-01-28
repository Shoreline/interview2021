# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Use a class member to save isBalanced and do quick return to avoid unnecessary computation
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        # Returns subtree height, AND also modifies self.balanced
        def dfs(root: TreeNode) -> int:
            if not self.balanced:  # if so, no need to proceed
                return -1

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                self.balanced = False
                return -1

            return 1 + max(left, right)

        dfs(root)
        return self.balanced

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         def dfs(root:TreeNode) -> int:
#             if not root:
#                 return 0

#             return 1 + max(dfs(root.left), dfs(root.right))

#         if not root:
#             return True

#         if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(dfs(root.left) - dfs(root.right)) <=1:
#             return True

#         return False

