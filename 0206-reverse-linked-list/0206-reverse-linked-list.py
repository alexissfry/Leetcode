# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        
        while(head):
            nodes.append(head.val)
            head = head.next 
        
        previous = None
        
        i = 0
        while i < len(nodes):
            previous = ListNode(nodes[i], previous)
            i += 1
        
        return previous