# Return a new linked list as the result

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_head = ListNode(0)
        tail = pre_head
        carry = 0
        while (l1 != None or l2 != None or carry != 0):
            sum = carry  # sum is the summation of current two nodes and the carry

            # Use two separate if blocks. Do addtion for non-null node(s)
            if (l1 != None):
                sum += l1.val
                l1 = l1.next
            if (l2 != None):
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            tail.next = ListNode(sum % 10)
            tail = tail.next

        return pre_head.next