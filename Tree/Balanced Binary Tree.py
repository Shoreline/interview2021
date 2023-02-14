# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time complexity is O(n), space complexity is O(h)
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

# Same execution speed (49ms)
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#
#         def get_height(root) -> int:
#             if not root:
#                 return 0
#
#             left = get_height(root.left)
#             right = get_height(root.right)
#
#             if left < 0 or right < 0 or abs(left - right) > 1:
#                 return -1
#             else:
#                 return 1 + max(left, right)
#
#         return get_height(root) >= 0

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

