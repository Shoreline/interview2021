# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Do reversed post-order traversal (root -> right -> left), then reverse the result
# Note that reversed post-order is not pre order!
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stack = [root]

        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.append(root.left)
                stack.append(root.right)

        return reversed(res)
