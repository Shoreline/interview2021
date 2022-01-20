# Idea

# Let dfs(left, right) return all valid BSTs where values in the BST in range [left..right].
# Then dfs(1, n) is our result.
# To solve dfs(left, right), we just
# Generate root value in range [left...right]
# Get left subtrees by leftNodes = dfs(left, root-1)
# Get right subtrees by rightNodes = dfs(root+1, right).
# Add all combination between leftNodes and rightNodes to form root trees.
# Can we cache the result of dfs(left, right) to prevent it to re-compute multiple time.
# There is a simillar problem, which is 894. All Possible Full Binary Trees, try to solve it yourself.

# Time: O(C0+C1+...Cn), where Cn is the Catalan number, n <= 8. Can check this problem 96. Unique Binary Search Trees to know why the number of nodes in the BST with n nodes is a Catalan number.
# The Catalan numbers for n = 0, 1, 2, 3, 4, 5, 6, 7, 8 are 1, 1, 2, 5, 14, 42, 132, 429, 1430.
# Space: O(n * Cn), there is total Cn BSTs, each BST has n nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from functools import lru_cache


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        # dfs() returns all valid BSTs where values in the BST in range [left..right]
        @lru_cache(None)
        def dfs(left, right):
            if left > right:
                return [None]  # can't be []
            if left == right:
                return [TreeNode(left)]  # BST has only one node, with val == left= =right

            res = []
            for root in range(left, right + 1):
                leftNodes = dfs(left, root - 1)
                rightNodes = dfs(root + 1, right)
                for leftNode in leftNodes:
                    for rightNode in rightNodes:
                        rootNode = TreeNode(root, leftNode, rightNode)
                        res.append(rootNode)
            return res

        return dfs(1, n)