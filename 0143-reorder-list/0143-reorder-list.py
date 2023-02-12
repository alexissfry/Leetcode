# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        current = head 
        host = []
        
        while current:
            host.append(current)
            current = current.next 
            
        if len(host) == 1:
            return head
        
        left = 0 
        right = len(host)-1
        
        while left <= right:
            host[left].next = host[right]
            # print(host[left].val,'points to', host[right].val)
            left += 1 
            host[right].next = host[left]
            # print(host[right].val,'points to', host[left].val)
            right -= 1
            if left == len(host)//2:
                # print(host[left].val,'points to none')
                host[left].next = None
                break
        
        
        return head 
        