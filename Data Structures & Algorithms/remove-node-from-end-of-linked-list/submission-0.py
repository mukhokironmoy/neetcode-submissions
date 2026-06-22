# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        slow = dummy
        fast = dummy

        # Move fast ahead by n spaces
        for i in range(n):
            fast = fast.next

        prev = None

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next

        return dummy.next
        