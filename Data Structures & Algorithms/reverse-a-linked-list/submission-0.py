# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = None
        curr2 = head

        while curr2:
            temp = curr2.next
            curr2.next = curr1
            curr1 = curr2
            curr2 = temp


        return curr1