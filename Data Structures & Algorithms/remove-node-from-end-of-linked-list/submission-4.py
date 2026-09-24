# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        while n > 0:
            head = head.next
            n -= 1

        p = dummy
        while head:
            p = p.next
            head = head.next
        
        p.next = p.next.next

        return dummy.next