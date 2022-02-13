# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# count the lengths of the two lists first
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        ptr = headA
        while ptr:
            lenA += 1
            ptr = ptr.next
        ptr = headB
        while ptr:
            lenB += 1
            ptr = ptr.next

        longer = headA if lenA > lenB else headB
        shorter = headA if lenA <= lenB else headB
        for i in range(abs(lenA - lenB)):
            longer = longer.next

        while longer and shorter and (longer != shorter):
            longer = longer.next
            shorter = shorter.next

        return longer


