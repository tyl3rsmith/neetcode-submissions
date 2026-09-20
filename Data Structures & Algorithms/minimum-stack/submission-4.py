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
        if not self.stack:
            self.stack.append(0)
            self.mini = val
        else:
            self.stack.append(val - self.mini)
            self.mini = min(self.mini, val)


    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()

        if pop < 0:
            self.mini -= pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.mini
        else:
            return self.mini

    def getMin(self) -> int:
        return self.mini