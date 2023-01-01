# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# For one node, you either rob it and not rob its children; or do not rob it, and keep the option to rob its children
#   - Therefore, for each node (or say subtree) return two values: max money you can rob 1) if you rob this node, or
#     2) you do not rob this node

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # Returns (rob_root, not_rob_root)
        @lru_cache(None)
        def helper(root) -> tuple[int, int]:
            if not root:
                return 0, 0
            # 1) If rob the root, you can't rob left and right
            rob_root = root.val + helper(root.left)[1] + helper(root.right)[1]
            # 2) If don't rob the root, you get to do whatever you want for its children.
            #    Rob/not_rob the left and rob/not_rob the right
            not_rob_root = max(helper(root.left)) + max(helper(root.right))

            return rob_root, not_rob_root

        return max(helper(root))

# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         res = self.helper(root)
#         return max(res[0], res[1])

#     def helper(self, root: TreeNode) -> List[int]:
#         if not root:
#             return [0, 0]

#         left = self.helper(root.left)
#         right = self.helper(root.right)

#         res = [0] * 2
#         res[0] = max(left[0], left[1]) + max(right[0], right[1])
#         res[1] = root.val + left[0] + right [0] # if rob root

#         return res
