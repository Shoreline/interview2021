# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(root: TreeNode, path: list[int]):
            if not root:
                return

            path.append(str(root.val))
            if not (root.left or root.right):
                val = str("".join(path))
                self.res += int(val)
            else:
                for child in (root.left, root.right):
                    dfs(child, path)
            path.pop()

        dfs(root, [])
        return self.res
