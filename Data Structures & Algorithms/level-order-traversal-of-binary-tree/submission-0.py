# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        result = []

        if root is None:
            return result

        # Initialise queue
        q1 = deque()
        q1.append(root)

        # Start processing
        while len(q1) != 0:
            level = []
            level_size = len(q1)

            for i in range(level_size):
                node = q1.popleft()
                level.append(node.val)

                if node.left is not None:
                    q1.append(node.left)

                if node.right is not None:
                    q1.append(node.right)

            result.append(level)

        return result
        