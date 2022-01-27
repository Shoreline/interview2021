# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The requirement is not a random BST, but a height-balanced binary search tree.
#   Use start/end to ensure heigh-balance.

# In-order simulation
# A sorted array is an inorder[]
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.pos = 0

        def inorder(start: int, end: int) -> TreeNode:
            if start > end:
                return None

            mid = start + (end - start) // 2

            left = inorder(start, mid - 1)  # order matters!
            root = TreeNode(nums[self.pos])
            self.pos += 1
            root.left = left
            root.right = inorder(mid + 1, end)

            return root

        return inorder(0, len(nums) - 1)

# A simpler way is to keep picking the middle element of a sub-array as the root
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         def helper(start:int, end:int) -> Optional[TreeNode]:
#             if start > end:
#                 return None

#             middle = (start + end) //2
#             root = TreeNode(nums[middle])
#             root.left = helper(start, middle - 1)
#             root.right = helper(middle+1, end)

#             return root

#         return helper(0,len(nums)-1)