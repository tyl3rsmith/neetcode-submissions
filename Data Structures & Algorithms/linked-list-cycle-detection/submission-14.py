# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() # set to track nodes we've seen
        curr = head
        while curr:
            if curr in seen: # we've already seen this node there's a cycle
                return True
            seen.add(curr) # mark this node as seen for future iterations
            curr = curr.next # check if the next node is a duplicate
        
        return False # if we made it here we broke out of the list so there was no cycle