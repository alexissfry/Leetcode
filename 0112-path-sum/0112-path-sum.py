# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, currSum):
            if not node:
                return False

            currSum += node.val

            if not node.left and not node.right:
                if currSum == targetSum:
                    return True

            return dfs(node.right, currSum) or dfs(node.left, currSum)

        return dfs(root,0)
