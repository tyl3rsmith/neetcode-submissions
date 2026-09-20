# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:   
        # Floyd's Tortoise and Hare Algorithm
        slow, fast = head, head # slow and fast pointers start at the start

        while fast and fast.next: # fast will reach null before slow, also check fast.next because we use fast.next.next in the loop body
            slow = slow.next # move slow by 1
            fast = fast.next.next # move fast by 2
            if slow == fast: # if there is a cycle eventually slow will equal fast
                return True
        return False

        