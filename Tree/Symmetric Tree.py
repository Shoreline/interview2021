# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time and space: n
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare(root1: TreeNode, root2: TreeNode) -> bool:
            if root1 and root2:
                return root1.val == root2.val and compare(root1.left, root2.right) and compare(root1.right, root2.left)
            elif root1 or root2:
                return False
            else:
                return True

        if not root:
            return True

        return compare(root.left, root.right)

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root == None:
#             return True

#         return self.compare(root.left, root.right)

#     def compare(self, root1: TreeNode, root2: TreeNode) -> bool:
#         if root1 == None and root2 == None:
#             return True
#         elif root1 == None or root2 == None or root1.val != root2.val:
#             return False

#         return self.compare(root1.left, root2.right) and self.compare(root1.right, root2.left)

