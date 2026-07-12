class MinStack:
    # Resolve using one stack
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append((val, val))
        else:
            min_val = min(val, self.stack[-1][1])
            self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        return self.stack[-1][1]
