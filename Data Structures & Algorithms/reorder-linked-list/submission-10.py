# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # break the list in half
        left = head
        mid = self.getMid(head)
        right = mid.next # guaranteed the len(left) >= len(right)
        mid.next = None # seperate the lists

        # reverse the second half
        right = self.reverseList(right)

        # merge the lists
        self.mergeLists(left, right)

    
    def getMid(self, head):
        # works for even and odd
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev
    
    def mergeLists(self, l1, l2):
        # 0 1 2 3
        # 6 5 4
        while l2: # we know the size of the right list (l2) is <= the size of the left list (l2)
            tmp1, tmp2 = l1.next, l2.next

            l1.next = l2
            l2.next = tmp1

            l1, l2 = tmp1, tmp2
        



