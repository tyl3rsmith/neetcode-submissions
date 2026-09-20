# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
            
        reverse = self.reverseList(head)

        curr = reverse

        i = 1
        if i == n:
            curr = curr.next
            return self.reverseList(curr)

        while i < n - 1:
            curr = curr.next
            i += 1

        if curr.next:
            curr.next = curr.next.next
        
        return self.reverseList(reverse)
    
    def reverseList(self, head):
        prev = None

        while head:
            head.next, prev, head = prev, head, head.next

        return prev