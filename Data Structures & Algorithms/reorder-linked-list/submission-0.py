# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle point of the list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None # pointer clean up of list1

        # reverse the second list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge the two halves
        first, second = head, prev

        while second: # we know the second half can be shorter than the first half
            tmp1, tmp2 = first.next, second.next
            first.next = second # merge
            second.next = tmp1
            # shift pointers
            first = tmp1
            second = tmp2

        

        
        