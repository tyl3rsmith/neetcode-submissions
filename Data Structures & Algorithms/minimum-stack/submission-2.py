class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        mini = self.stack[-1]
        for n in self.stack:
            mini = min(n, mini)
        
        return mini

        # 2, 3, 1, 4, 5
        # mini = 5
        # tmp = [5]