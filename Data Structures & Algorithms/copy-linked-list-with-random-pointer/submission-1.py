"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}

        p = head

        while p:
            map[p] = Node(p.val, None, None)
            p = p.next
        
        p = head

        while p:
            node = map[p]
            if p.next:
                node.next = map[p.next]
            if p.random:
                node.random = map[p.random]
            p = p.next
    
        return map[head] if head else None