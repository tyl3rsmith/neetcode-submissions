# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list1 = head

        # find the second list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # seperate the lists into two
        list2, slow.next = slow.next, None

        # reverse the second list
        prev, curr = None, list2
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        # prev points at the start of the reversed list
        list2 = prev
        while list2:
            list1.next, list2.next, list1, list2 = list2, list1.next, list1.next, list2.next
