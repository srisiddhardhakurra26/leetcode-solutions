# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy
        carry = 0
        
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            total = l1Val + l2Val + carry
            carry = total // 10
            total = total % 10

            res.next = ListNode(total)
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
