class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.mini = val
        else:
            self.stack.append(val - self.mini)
            if val < self.mini:
                self.mini = val

    def pop(self) -> None:
        pop = self.stack.pop()

        if pop < 0:
            self.mini = self.mini - pop

    def top(self) -> int:
        top = self.stack[-1]

        if top < 0:
            return self.mini
        else:
            return self.mini + top

    def getMin(self) -> int:
        return self.mini



# push 5
# [0] min = 5 

# push 6
# [0, 1] min = 5

# push 7
# [0, 1, 2] min = 5

# push 3
# [0, -2] min = 3

# push 2
# [0, -2, -1] min = 2