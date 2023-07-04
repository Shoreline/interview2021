# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# Time O(N), Space O(height)
# (0-based index) A complete binary tree can be represented with an array. If the index of a node in the array is i, the element at index 2i + 1 will be its left child and the element at index 2i + 2 will be its right child.
#
# Here we use 1-based index
class Solution:
    def isCompleteTree(self, root):
        # returns: number of nodes, right_most_coords
        # coord: 1-based index
        def dfs(root, coord):
            if not root:
                return 0, 0
            l = dfs(root.left, 2 * coord)
            r = dfs(root.right, 2 * coord + 1)

            tot = l[0] + r[0] + 1
            right_most = max(coord, l[1], r[1])  # rightmost index
            return tot, right_most

        if not root:
            return True
        tot, right_most = dfs(root, 1)  # root is 1, not 0 -> coord is 1-based index
        return tot == right_most


# BFS
# Time O(N), Space O(N)
class Solution2:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])  # there should not be any node after we met an empty one.