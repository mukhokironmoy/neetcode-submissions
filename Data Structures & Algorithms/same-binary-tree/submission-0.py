# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque

        q1 = deque()
        q1.append((p,q))

        while q1:
            node1, node2 = q1.popleft()

            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            q1.append((node1.left, node2.left))
            q1.append((node1.right, node2.right))

        return True
        
        # if p is None and q is None:
        #     return True

        # if p is None or q is None:
        #     return False

        # if p.val != q.val:
        #     return False

        # left_same = self.isSameTree(p.left, q.left)
        # right_same = self.isSameTree(p.right, q.right)

        # return left_same and right_same
        