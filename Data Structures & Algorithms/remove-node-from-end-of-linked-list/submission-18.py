# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None

        # Reverse the list
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        newHead = prev

        # Find the node to remove
        curr = newHead
        parent = None

        while n > 1:
            parent = curr
            curr = curr.next
            n -= 1

        # Remove the node
        if parent is None:
            newHead = curr.next
        else:
            parent.next = curr.next

        # Reverse the list again
        prev = None
        while newHead:
            temp = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = temp

        return prev