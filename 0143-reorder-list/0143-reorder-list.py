# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        s = slow.next
        slow.next = prev = None
        while s:
            temp = s.next
            s.next = prev
            prev = s
            s = temp
        
        second = prev
        first = head
        while second:
            tempf, temps = first.next, second.next
            first.next = second
            second.next = tempf
            first, second = tempf, temps
        
        return head