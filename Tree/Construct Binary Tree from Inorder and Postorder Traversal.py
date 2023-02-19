# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Note that values in postorder[] and inorder[] are set to be unique
# Key: build map<value, index> of the inorder traversal array
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # all parameters are indice in traversal arrays
        def helper(post_root: int, in_start: int, in_end: int) -> TreeNode:
            if in_start > in_end:
                return None

            root = TreeNode(postorder[post_root])

            in_root = in_map[root.val]
            right_sub_tree_len = in_end - in_root

            root.right = helper(post_root - 1, in_root + 1, in_end)
            root.left = helper(post_root - 1 - right_sub_tree_len, in_start, in_root - 1)

            return root

        in_map = {}
        for i, val in enumerate(inorder):
            in_map[val] = i

        return helper(len(postorder) - 1, 0, len(inorder) - 1)