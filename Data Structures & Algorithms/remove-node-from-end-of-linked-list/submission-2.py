# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass
        p = head
        count = 0
        while p:
            p = p.next
            count += 1
            
        if count < n:
            return None
        
        count = count - n - 1

        p = head

        if count < 0: # remove first node
            return p.next

        while count > 0:
            p = p.next
            count -= 1

        # remove next node
        p.next = p.next.next

        return head
        



        