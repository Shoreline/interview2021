# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# /*
#  * http://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-
#  * statistics-in-bst/
#  *
#  * For the follow up: add a field to save the left subtree size in every node.
#  *
#  * Assume that the root is having N nodes in its left subtree. If K = N + 1,
#  * root is K-th node. If K < N, we will continue our search (recursion) for the
#  * Kth smallest element in the left subtree of root. If K > N + 1, we continue
#  * our search in the right subtree for the (K – N – 1)-th smallest element
#  */

# Iterative inorder traverse
# t: O(H+k): H is tree height. k is the input ("k"-th smallest)
# s: O(H): stack has at most H elements

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        while root or stack:
            if not root:
                root = stack.pop()
                if k == 1:
                    return root.val
                k -= 1
                root = root.right
            else:
                stack.append(root)
                root = root.left

        return -1

# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         count = 0
#
#         def inorder(root: TreeNode) -> int:
#             nonlocal count
#             if not root:
#                 return None
#
#             val = inorder(root.left)
#             if val != None:  # "if val" does not work
#                 return val
#             count += 1
#             if count == k:
#                 return root.val
#             return inorder(root.right)
#
#         return inorder(root)

    # class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         stack = [] # stack to save the visited root nodes
#         cur = root
#         count = 0
#         while cur or stack:
#             if cur:
#                 stack.append(cur)
#                 cur = cur.left
#             else:
#                 node = stack.pop()
#                 count += 1
#                 if count == k:
#                     return node.val
#                 cur = node.right

#         return -sys.maxsize

