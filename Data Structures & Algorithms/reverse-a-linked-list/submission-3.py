# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive approach
        # base cases: head is null or head.next is null
        # sub problem: reverse list without head included (sub lists)

        if (not head or not head.next):
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newHead