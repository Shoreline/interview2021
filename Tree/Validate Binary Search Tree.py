# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# t and s: O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], min_val: int, max_val: int) -> bool:
            if not root:
                return True
            elif root.val <= min_val or root.val >= max_val:
                return False
            else:
                return helper(root.left, min_val, root.val) and helper(root.right, root.val, max_val)

        return helper(root, -float('inf'), float('inf'))

# a wrong example, easy to make such mistake
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:

#         if not root:
#             return True
#         if root.left and root.left.val >= root.val:
#             return False
#         if root.right and root.right.val <= root.val: #wrong! right must 1) > root; 2) < root of root
#             return False

#         return self.isValidBST(root.left) and self.isValidBST(root.right)
