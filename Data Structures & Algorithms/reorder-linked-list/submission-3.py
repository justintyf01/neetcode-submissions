# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return None

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # start of 2nd half
        prev = slow.next = None

        while second: # reverse second half
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge
        l1, l2 = head, prev
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next, l2.next = l2, tmp1
            l2, l1 = tmp2, tmp1
        


            


        

