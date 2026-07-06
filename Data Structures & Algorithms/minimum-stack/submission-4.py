class MinStack:
    # O(1) using only 1 stack
    def __init__(self):
        self.stack = []
        self.min_value = float('inf')

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append(0)
            self.min_value = val
        else:
            self.stack.append(val - self.min_value)
            self.min_value = min(self.min_value, val)

    def pop(self) -> None:
        if self.stack == []:
            return
        
        popped = self.stack.pop()

        if popped < 0:
            self.min_value = self.min_value - popped

    def top(self) -> int:
        if self.stack[-1] > 0:
            return self.stack[-1] + self.min_value
        else:
            return self.min_value

    def getMin(self) -> int:
        return self.min_value
