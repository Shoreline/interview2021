# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        target = set(to_delete)

        def helper(node, parent_node):
            if not node:
                return

            delete = False
            if node.val not in target and not parent_node:
                res.append(node)
            elif node.val in target:
                delete = True
                if parent_node:
                    if node == parent_node.left:
                        parent_node.left = None
                    else:
                        parent_node.right = None

            if delete:
                helper(node.left, None)
                helper(node.right, None)
            else:
                helper(node.left, node)
                helper(node.right, node)

        helper(root, None)
        return res

