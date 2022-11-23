# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val: #if the root is bigger than both nodes 
            return self.lowestCommonAncestor(root.left,p,q) #both nodes must be to the left of root
        elif root.val < p.val and root.val < q.val: #if the root is smaller than both nodes
            return self.lowestCommonAncestor(root.right,p,q) #both nodes must be to the right of the root
        return root #otherwise the nodes are on either side of the root or one of the nodes is the root, so we return the root
        