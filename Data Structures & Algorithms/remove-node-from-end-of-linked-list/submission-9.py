# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        removeIdx = length - n
        if removeIdx == 0:
            return head.next

        curr = head
        for i in range(length - 1):
            if (i + 1) == removeIdx:
                curr.next = curr.next.next
                break
            curr = curr.next
    
        return head