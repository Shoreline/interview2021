"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


# We are ensured that p and q exist in the tree.
# almost the same as https://leetcode.com/problems/intersection-of-two-linked-lists/

# O(N) space solution
# Record the path from node p to root. (O(N) space, N is length of path P)
# Traverse from node q to root and find the first common point.

# O(1) space solution 1
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        depthP, depthQ = 0, 0
        cur = p
        while cur.parent != None:
            cur = cur.parent
            depthP += 1
        cur = q
        while cur.parent != None:
            cur = cur.parent
            depthQ += 1

        # let p and q have the same depth
        diff = abs(depthP - depthQ)
        if depthP > depthQ:
            for i in range(diff):
                p = p.parent
        else:
            for i in range(diff):
                q = q.parent

        while p != q:
            p = p.parent
            q = q.parent

        return p

# O(1) space solution 2
# Since it is guaranteed that there will be a LCA, we can use two pointers for each list. When we reach the end of one list, switch it to point at the beginning of the other list until p1 is p2.
# class Solution:
#     def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
#         p1, p2 = p, q
#         while p1 != p2:
#             print(p1.val, ' ',p2.val)
#             p1 = p1.parent if p1.parent else q
#             p2 = p2.parent if p2.parent else p

#         return p1
