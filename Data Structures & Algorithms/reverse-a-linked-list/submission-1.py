# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        prev = None
        curr = head
        head = head.next

        while head:
            curr.next = prev
            prev = curr
            curr = head
            head = head.next
            
        if not head:
            curr.next = prev
            return curr

        return head



            
