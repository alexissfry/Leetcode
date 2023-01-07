# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        def rec(node):
            if node is None:
                return None

            if val < node.val:
                return rec(node.left)
            elif val > node.val:
                return rec(node.right)
            else:
                return node
        
        return rec(root)