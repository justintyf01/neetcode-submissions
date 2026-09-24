# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        p = head
        while p: # 1st pass to put into stack
            stack.append(p)
            p = p.next
        
        if len(stack) <= 2:
            return None
        
        c = len(stack) // 2
        
        p = head # reinit pointer
        for i in range (c + 1):
            tmp = p.next
            last = stack.pop()
            p.next = last
            last.next = tmp
            p = p.next.next

        p.next = None
        return None
        
        