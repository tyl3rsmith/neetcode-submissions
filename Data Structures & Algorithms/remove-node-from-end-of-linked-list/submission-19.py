# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Compute the length
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        
        # Compute the remove index
        remove_index = length - n

        if remove_index == 0:
            return head.next
        
        # Go to spot right before remove index
        curr = head
        while remove_index > 1:
            curr = curr.next
            remove_index -= 1
        
        # Remove the element
        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return head

