# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def pre_order(node):
            
            if node is None:
                return "_"
            
            out = ""

            out += f"{node.val}"
            out += pre_order(node.left)
            out += pre_order(node.right)

            return out

        tree_str = pre_order(root)
        subtree_str = pre_order(subRoot)

        if subtree_str in tree_str:
            return True
        else:
            return False

        