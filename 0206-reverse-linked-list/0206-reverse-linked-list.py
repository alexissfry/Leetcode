# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return
        
        nodes = []
        
        while(head):
            nodes.append(head.val)
            head = head.next 
        
        reverse = []
        reverse.append(ListNode(nodes[0],None))
        i = 1
        while i < len(nodes):
            reverse.append(ListNode(nodes[i], reverse[i-1]))
            i += 1
        
        return reverse[len(reverse)-1]