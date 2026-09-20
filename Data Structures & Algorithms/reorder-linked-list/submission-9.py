# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # break lists into two
        leftList = head
        mid = self.getMid(head)
        rightList = mid.next
        mid.next = None

        # reverse the second half
        rightList = self.reverseList(rightList)

        # merge the lists
        self.mergeLists(leftList, rightList)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head):
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next

        return prev
    
    def mergeLists(self, l1, l2):
        # 0 -> 1 -> 2 -> 3
        # 6 -> 5 -> 4

        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1, l2 = temp1, temp2
