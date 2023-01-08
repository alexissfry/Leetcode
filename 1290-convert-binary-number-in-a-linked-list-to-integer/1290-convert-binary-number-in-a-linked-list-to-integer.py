# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        size = 0
        decimal = 0

        current = head
        while current:
            size += 1
            current = current.next 
        
        while head:
            size -= 1
            
            if head.val == 1:
                decimal += 2**size
            
            head = head.next 
        
        return decimal 
            