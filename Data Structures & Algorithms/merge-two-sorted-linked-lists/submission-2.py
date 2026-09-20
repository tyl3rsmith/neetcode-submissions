# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while list1 and list2:
            if list1.val < list2.val:
                arr.append(list1.val)
                list1 = list1.next
            else:
                arr.append(list2.val)
                list2 = list2.next
        
        if list1:
            while list1:
                arr.append(list1.val)
                list1 = list1.next
        elif list2:
            while list2:
                arr.append(list2.val)
                list2 = list2.next

        res = ListNode()
        temp = res

        for num in arr:
            node = ListNode(num)     
            temp.next = node
            temp = temp.next

        return res.next   