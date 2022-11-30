# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #preorder goes root, left, right

        def helper(node):
            if not node:
                return []
            
            traversal = []
            
            traversal.append(node.val)
            
            for value in helper(node.left):
                traversal.append(value)

            for value in helper(node.right):
                traversal.append(value)
            return traversal
        
        return helper(root)