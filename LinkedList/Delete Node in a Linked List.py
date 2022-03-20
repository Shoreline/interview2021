# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# The purpose is not to actually delete the given node, but copy the next node's value to the given node,
# then delete the next node.
# That's why the problem statement emphasis that the given node is surly not the tail node.
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next