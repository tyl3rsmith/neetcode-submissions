# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            return self.reverseList(self.reverseList(head).next)
            
        reverse = self.reverseList(head)
        curr = reverse

        i = 1
        while i < n - 1:
            curr = curr.next
            i += 1

        curr.next = curr.next.next
        
        return self.reverseList(reverse)
    
    def reverseList(self, head):
        prev = None

        while head:
            head.next, prev, head = prev, head, head.next

        return prev