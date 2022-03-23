# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(tmp: list[str], root: Optional[TreeNode]):
            if not root:
                return

            tmp.append(str(root.val))
            if (not root.left) and (not root.right):
                res.append("->".join(tmp))
            else:
                dfs(tmp, root.left)
                dfs(tmp, root.right)
            tmp.pop()

        dfs([], root)
        return res