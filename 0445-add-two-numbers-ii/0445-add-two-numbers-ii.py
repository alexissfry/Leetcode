# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = ""
        list2 = ""

        while l1:
            list1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            list2 += str(l2.val)
            l2 = l2.next
        
        sumLists = int(list1) + int(list2)
        stringSum = str(sumLists)

        finalSum = ListNode(int(stringSum[0]))
        head = finalSum 
        for i in range(1,len(stringSum)):
            finalSum.next = ListNode(int(stringSum[i]))
            finalSum = finalSum.next

        return head