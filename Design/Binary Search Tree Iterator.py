# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Stack solution
# next() takes O(N), but constructor takes O(1)
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = []  # saves the parent nodes

    def next(self) -> int:  # PS says it is always valid
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        self.cur = self.stack.pop()
        res = self.cur.val
        self.cur = self.cur.right  # once we move cur to a right subtree, the left subtree won't be visited again

        return res

    def hasNext(self) -> bool:
        return self.cur or self.stack

# Another solution is to do in-order traverse in constructor and saves result in a list
# then next() takes O(1), but constructor takes O(N)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()