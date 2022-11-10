# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if node is None:
                return -1
            if node.left == None and node.right == None:
                return 0
            return max(height(node.left), height(node.right)) + 1

        def dfs(node):
            if node is None:
                return True

            if abs(height(node.left) - height(node.right)) > 1:
                return False
            
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root)