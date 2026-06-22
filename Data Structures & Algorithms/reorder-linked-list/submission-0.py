# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_mid(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        return mid

    def reverse_from_mid(self, mid):
        prev = None
        cur = mid

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.find_mid(head)

        tail = self.reverse_from_mid(mid)

        dummy = ListNode()
        cur = dummy

        while head and tail:
            cur.next = head
            head = head.next

            cur.next.next = tail
            tail = tail.next
            cur = cur.next.next

        if head:
            cur.next = head



            
        