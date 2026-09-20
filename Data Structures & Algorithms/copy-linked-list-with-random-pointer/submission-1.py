"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        # copy each node
        curr = head
        while curr:
            # if we haven't made a copy yet make a copy
            if curr not in oldToCopy:
                oldToCopy[curr] = Node(curr.val)

            copy = oldToCopy[curr]
            
            # copy the next and random pointer
            if curr.next not in oldToCopy:
                oldToCopy[curr.next] = Node(curr.next.val)
            
            copy.next = oldToCopy[curr.next]

            if curr.random not in oldToCopy:
                oldToCopy[curr.random] = Node(curr.random.val)

            copy.random = oldToCopy[curr.random]

            # try to clone the next node
            curr = curr.next
        
        return oldToCopy[head]