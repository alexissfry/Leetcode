# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = {}
        
        while head:
            if head not in cycle:
                cycle[head] = head.next 
            else:
                return True
            head = head.next
            
        return False 