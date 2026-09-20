# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle point
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None # seperate the lists

        # reverse the second half
        prev = None

        while second:
            second.next, prev, second = prev, second, second.next
        
        first, second = head, prev

        # merge the lists
        while second:
            t1 = first.next
            t2 = second.next

            first.next, second.next = second, first.next
            first, second = t1, t2
