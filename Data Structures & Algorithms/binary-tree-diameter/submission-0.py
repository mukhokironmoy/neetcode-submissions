# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def height(root, diameter:list):
            if root is None:
                return 0

            left_height = height(root.left, diameter)
            right_height = height(root.right, diameter)

            diameter[0] = max(diameter[0], left_height+right_height)

            return 1+max(left_height, right_height)

        height(root, diameter)

        return diameter[0]
        