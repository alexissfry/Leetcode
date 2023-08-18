# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        maxSum = -inf
        levelCount = 0
        maxLevel = 0

        queue.append(root)

        while queue:
            level = 0
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levelCount += 1 

            if level > maxSum:
                maxSum = level
                maxLevel = levelCount
            print(maxSum, maxLevel)

        return maxLevel