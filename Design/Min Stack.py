# The only difference between minStack and normal stack is that minStack has getMin()
# getMin() is an operation of peek, no need to pop anything.
# use two stacks (implemented by two lists)

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack or (val <= self.min_stack[-1]):
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:  # Can use ==. Update github Java solution?
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None