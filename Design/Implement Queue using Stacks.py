class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if self.out:
            return self.out.pop()

        while self.in_stack:
            self.out.append(self.in_stack.pop())

        return self.out.pop() if self.out else -1

    def peek(self) -> int:
        if self.out:
            return self.out[-1]

        while self.in_stack:
            self.out.append(self.in_stack.pop())

        return self.out[-1] if self.out else -1

    def empty(self) -> bool:
        return not (self.in_stack or self.out)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()