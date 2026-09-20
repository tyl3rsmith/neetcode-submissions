class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        # possibility the new val could be a new min

        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # optimized approach
        # we maintain 2 stacks
        # one tracks the regular elements
        # the other will track the current minimum at each point so we can access in O(1)

        return self.minStack[-1]