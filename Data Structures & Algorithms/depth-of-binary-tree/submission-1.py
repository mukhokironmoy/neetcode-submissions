# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if root is None:
            return 0

        q1 = deque()
        q1.append(root)
        level = 0

        while len(q1)!= 0:
            level_size = len(q1)

            for i in range(level_size):
                node = q1.popleft()

                if node.left is not None:
                    q1.append(node.left)

                if node.right is not None:
                    q1.append(node.right)

            level+= 1

        return level

        # if root is None:
        #     return 0

        # left_height = self.maxDepth(root.left)
        # right_height = self.maxDepth(root.right)

        # return 1 + max(left_height, right_height)
        