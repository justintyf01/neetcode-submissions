# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set([])

        if not head:
            return False

        idx = 0
        while head.next is not None:
            seen.add(head)
            head = head.next

            if head in seen:
                return True

        return False