# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        lca = None

        def dfs(node):
            # take in a node
            # return a tuple (ancestorP, ancestorQ)
            # which returns whether this node is an ancestor of P and/or an ancestor of Q
            # we will also update lca if this is the lowest common ancestor of p and q
            nonlocal lca
            ancestorP = False
            ancestorQ = False

            if not node:
                return (False, False)

            if node == p:
                ancestorP = True
            if node == q:
                ancestorQ = True
            
            leftAncestorP, leftAncestorQ = dfs(node.left)
            rightAncestorP, rightAncestorQ = dfs(node.right)

            if leftAncestorP or rightAncestorP:
                ancestorP = True
            
            if leftAncestorQ or rightAncestorQ:
                ancestorQ = True

            if ancestorP and ancestorQ and lca == None:
                lca = node 
                return (True,True) 

            return (ancestorP, ancestorQ)

        dfs(root)
        return lca
        '''
        parent_val = root.val
        p_val = p.val
        q_val = q.val

        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)

        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return root