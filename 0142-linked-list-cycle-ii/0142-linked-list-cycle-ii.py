# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mapNodes = {}
        current = head 
        
        if current is None:
            return None 
        
        while current.next:
            mapNodes[current] = current.next 
            
            if current.next in mapNodes.keys():
                return current.next
            
            current = current.next 
        
        return None
            