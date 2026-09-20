class MinStack:
    # The key trick is using only one stack (instead of two),
    # by storing differences between values and the current minimum,
    # rather than raw values.

    # 1 2 3
    # 0 1 2
    # 1 1 1

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if val <= self.mini:
            self.stack.append(self.mini)
            self.mini = val
        self.stack.append(val)

    def pop(self) -> None:
        if (self.stack.pop() == self.mini):
            self.mini = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini