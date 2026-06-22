# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            addition = (l1.val + l2.val + carry_over) % 10
            cur.next = ListNode(addition)
            carry_over = (l1.val + l2.val + carry_over) // 10

            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            addition = (l1.val + carry_over) % 10
            cur.next = ListNode(addition)
            carry_over = (l1.val + carry_over) // 10

            cur = cur.next
            l1 = l1.next

        while l2:
            addition = (l2.val + carry_over) % 10
            cur.next = ListNode(addition)
            carry_over = (l2.val + carry_over) // 10

            cur = cur.next
            l2 = l2.next

        while carry_over:
            addition = carry_over % 10
            cur.next = ListNode(addition)
            carry_over = carry_over // 10

        return dummy.next
        