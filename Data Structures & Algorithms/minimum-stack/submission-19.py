class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # min element from [0:i]
    
    def push(self, val: int) -> None:
        if self.minStack and val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1] if self.minStack else val)

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]