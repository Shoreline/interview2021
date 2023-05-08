# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def helper(root, tmp, target):
            if not root:
                return

            tmp.append(root.val)
            target -= root.val
            if not (root.left or root.right) and target == 0:
                res.append(tmp[:])
            else:
                helper(root.left, tmp, target)
                helper(root.right, tmp, target)
            tmp.pop()

        helper(root, [], targetSum)
        return res

# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#
#         res = []
#
#         def dfs(root: TreeNode, rem_target: int, tmp: list[int]):
#             if not root:
#                 return
#
#             tmp.append(root.val)
#
#             if (not root.left) and (not root.right) and rem_target == root.val:
#                 res.append(tmp[:])
#                 # If we want to return here, need to do tmp.pop() first.
#                 # This is because this if block is run after tmp[] appending in dfs().
#             else:
#                 for child in (root.left, root.right):
#                     dfs(child, rem_target - root.val, tmp)
#
#             tmp.pop()
#
#         dfs(root, targetSum, [])
#         return res

# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

#         res = []
#         def dfs(root:TreeNode, rem_target:int, tmp:list[int]):
#             if not root:
#                 return
#             if (not root.left) and (not root.right) and rem_target == root.val:
#                 tmp.append(root.val)
#                 res.append(tmp[:])
#                 tmp.pop() # easy to miss
#                 return

#             tmp.append(root.val)
#             for child in (root.left, root.right):
#                 dfs(child, rem_target - root.val, tmp)
#             tmp.pop()

#         dfs(root, targetSum, [])
#         return res