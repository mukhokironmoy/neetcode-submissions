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
        if head is None:
            return None

        cur = head

        # Create the new nodes ahead of the current ones
        while cur:
            new_node = Node(cur.val, cur.next)
            cur.next = new_node
            cur = new_node.next

        cur = head
        
        # Map the random pointers
        while cur:
            if cur.random is None:
                cur.next.random = None
            else:
                cur.next.random = cur.random.next

            cur = cur.next.next

        cur = head
        new_head = head.next
        new_cur = new_head

        # Separate the lists
        while new_cur:
            cur.next = new_cur.next
            cur = cur.next

            if cur is None:
                new_cur.next = None
            else:
                new_cur.next = cur.next

            new_cur = new_cur.next
        
        return new_head
        