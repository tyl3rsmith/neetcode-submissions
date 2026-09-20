# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        carry = 0

        while l1 or l2 or carry:
            # edge cases:
            # len of l1 and l2 different one can be null (use 0 for its val)
            # we have a final carry even when we are done adding l1 and l2
            # we process the last carry as use v1 and v2 as 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            curr.next = ListNode(val)

            curr = curr.next
            # only update these next pointers if they are non null bc
            # from the edge cases l1 and l2 can be null
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next