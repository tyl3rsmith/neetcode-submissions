# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2 pointer iterative approach
        prev, cur = None, head

        while cur:
            temp = cur.next # save this so we can shift cur over
            cur.next = prev # reverse the next pointer
            prev = cur # shift prev and cur
            cur = temp
        
        return prev

        
        