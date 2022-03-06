# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Level order traverse
#  two lists: cur_lvl and next_lvl
# T: O(N); S: O(n/2)-> O(n). There can be at most n/2 nodes on one level
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        cur_lvl = [root]
        while cur_lvl:
            next_lvl = []
            for node in cur_lvl:
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            res.append(cur_lvl[-1].val)
            cur_lvl = next_lvl

        return res