# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle point of the list
        slow, fast = head, head
    
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        second = slow

        while second:
            second.next, prev, second = prev, second, second.next
        
        first = head
        second = prev

        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        
        

        
        