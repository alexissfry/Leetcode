# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            if left == None and right == None:
                return True
            if (left == None and right != None) or (left != None and right == None):
                return False
            else:
                if left.val == right.val:
                    return isMirror(left.left, right.right) and isMirror(left.right, right.left)
                else:
                    return False
        
        return isMirror(root.left,root.right)