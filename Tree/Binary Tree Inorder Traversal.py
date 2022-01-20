# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 3 Solutions: Morris traversal; recursion, iteration (use a stack).
# /*
#  * Recursion solution O(N) time, O(logN) space
#  * O(N) time: total N nodes, visit each one once.
#  * O(logN) space (avg): tree height is logN, so maximum logN layers of recursion.
#  Worst case space O(N)
#  */

# Recursion 1
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         def helper(root:TreeNode):
#             if root:
#                 helper(root.left)
#                 res.append(root.val)
#                 helper(root.right)

#         res = []
#         helper(root)
#         return res

# /*
#  * Iterative method: use a stack.
#  *
#  * O(N) time, O(logN) space
#  *
#  * Besides the Stack, also need to keep track a pointer (root). Each
#  * iteration, operates on the pointer node.
#  */
# Iterative method for pre/in/post order traversal:
# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/713539/Python-3-All-Iterative-Traversals-InOrder-PreOrder-PostOrder-Similar-Solutions
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur != None or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res

# Recursion 2
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         self.recursion(root, res)
#         return res

#     def recursion(self, root: TreeNode, res: List[int]):
#         if root == None:
#             return

#         self.recursion(root.left, res)
#         res.append(root.val)
#         self.recursion(root.right, res)
#         return

# /*
#  * Morris Traversal: O(N) time (actually is O(2N)); O(1) space
#  *
#  * http://blog.csdn.net/linhuanmars/article/details/20187257
#  *
#  * Only use two additional variables.
#  */