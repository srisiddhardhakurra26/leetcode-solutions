# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        head2 = dummy

        while cur:
            if cur.val == val:
                head2.next = cur.next
            else:
                head2 = cur
            cur = cur.next
        return dummy.next