# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def dfs(node, level):
            
            if not node:
                return None
            
            if len(levels) == level:
                levels.append([])
                            
            dfs(node.left, level+1)            
            dfs(node.right, level+1)
        
            levels[level].append(node.val)

            
            
        dfs(root,0)
        
        return levels
    
        
            