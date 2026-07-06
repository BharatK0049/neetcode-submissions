class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append((val, val))
        else:
            min_val = self.stack[-1][1] # Current top of stack and the min at last
            self.stack.append((val, min(min_val, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
