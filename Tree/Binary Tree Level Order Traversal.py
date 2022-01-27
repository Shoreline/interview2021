# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# t and s: O(n)
# #deque #shallow copy
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = deque([root])

        while q:
            cur_lvl_nodes = len(q)
            new_lvl = []
            res.append(new_lvl)  # shallow copy. Later changes made to new_lvl will be reflected in res

            for i in range(cur_lvl_nodes):
                node = q.popleft()
                new_lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         res = []
#         if not root:
#             return res

#         q = deque([root])

#         while len(q) > 0:
#             new_lvl = []
#             res.append(new_lvl)
#             cur_queue_len = len(q)

#             for i in range(cur_queue_len):
#                 node = q.popleft()
#                 new_lvl.append(node.val)

#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)

#         return res


# Or use cur_lvl_list and next_lvl_list        