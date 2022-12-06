# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, up):
            if not node:
                return True
            if not low < node.val < up:
                return False
            
            return valid(node.left, low, node.val) and valid(node.right, node.val, up)
            
        
        return valid(root, -math.inf, math.inf)