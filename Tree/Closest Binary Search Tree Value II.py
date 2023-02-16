# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(N) time and O(k) space
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        values = deque([])

        # In-order traversal of a BST will give us a sorted array
        # Note that values always keep a sorted set of values.
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if len(values) == k:
                if abs(root.val - target) < abs(values[0] - target):
                    values.popleft()
                else:
                    return
            values.append(root.val)
            inorder(root.right)

        inorder(root)
        return list(values)

# Simply traverse all tree nodes while maintain a heap of size k
#   The heap element is a tuple: ( negative_distance, node_value)
# Time: O(Nlogk); S: O(k+H) H is the tree height
# import heapq
# class Solution:
#     def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
#         def inorder(root: TreeNode):
#             if not root:
#                 return
#
#             inorder(root.left)
#             heappush(heap, (- abs(root.val - target), root.val))
#             if len(heap) > k:
#                 heappop(heap)
#             inorder(root.right)
#
#         heap = []
#         inorder(root)
#         return [x for _, x in heap]  # _ is the negative_distance
