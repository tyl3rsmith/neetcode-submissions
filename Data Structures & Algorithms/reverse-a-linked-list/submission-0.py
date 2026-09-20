class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        # Convert linked list to array
        while head:
            arr.append(head.val)
            head = head.next

        # Return None if the list is empty
        if not arr:
            return None

        # Create the new reversed list
        res = ListNode(arr[0])
        current = res

        for val in arr[1:]:
            node = ListNode(val)
            node.next = current
            current = node

        return current
