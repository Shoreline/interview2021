# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Note that values in preorder[] and inorder[] are set to be unique
# 1) The first element in preorder[] is the root of the tree
# 2) In inorder[], values before the root are the nodes of the left subtree; values after are the right subtree
# So, the key is to find the root, and then find the index of the root in inorder[]

# /*
#  * Keep track of the index range of current subtree in int[] preorder and int[]
#  * inorder.
#  *
#  * Each time being invoked, the helper method build the root node of current
#  * subtree, then call itself twice to continuously build root.left and
#  * root.right
#  */

# t and s: O(N). maps takes O(n) space; recursion depth is O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def helper(pre_start: int, in_start: int, in_end: int) -> TreeNode:
            if in_start > in_end:
                return None
            root = TreeNode(preorder[pre_start])
            root_inorder_index = inorder_index_map[root.val]
            left_subtree_length = root_inorder_index - in_start  # number of nodes in the left subtree

            root.left = helper(pre_start + 1, in_start, root_inorder_index - 1)
            root.right = helper(pre_start + 1 + left_subtree_length, root_inorder_index + 1, in_end)

            return root

        inorder_index_map = {}  # map<value, inorder_index>
        for i in range(len(inorder)):
            inorder_index_map[inorder[i]] = i

        return helper(0, 0, len(inorder) - 1)

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         inorder_idx_map = {} # key: value of each tree node; value: index in the inorder array
#         for i in range(len(inorder)):
#             inorder_idx_map[inorder[i]] = i

#         return self.treeBuilder(preorder, 0, inorder, 0, len(inorder) - 1, inorder_idx_map)

#     def treeBuilder(self, preorder: List[int], preStart:int, inorder: List[int], inStart:int, inEnd:int, inorder_idx_map) -> TreeNode:
#         if inStart > inEnd:
#             return None

#         root = TreeNode(preorder[preStart])
#         root_inorder_idx = inorder_idx_map[root.val]
#         lenLeft = root_inorder_idx - inStart # number of elements in the left subtree

#         root.left = self.treeBuilder(preorder, preStart + 1, inorder, inStart, root_inorder_idx -1, inorder_idx_map)
#         root.right = self.treeBuilder(preorder, preStart + 1 + lenLeft, inorder, root_inorder_idx + 1, inEnd, inorder_idx_map)

#         return root