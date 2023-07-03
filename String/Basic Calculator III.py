# Recursion
class Solution:
    def calculate(self, s: str) -> int:
        # stack saves oprand values that will be added together for final result
        # sign is previous sign
        num, stack, sign = 0, [], "+"
        s += 'E'  # final wrap up when i == len(s)-1
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '(':
                # recursively call itself to compute result between parentheses
                num, skip = self.calculate(s[i + 1:])
                i += skip
            elif s[i] in '+-*/)' or i == len(s) - 1:
                # While meeting a new sign / ')' or end of input string
                # Need to compute based on previous oprands and previous sign
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:  # sign == '/'
                    stack.append(int(stack.pop() / num))

                if s[i] == ')':
                    return sum(stack), i + 1

                # current operation is done, reset num and sign
                num = 0
                sign = s[i]

            i += 1

        return sum(stack)


class Solution2:
    def calculate(self, s: str) -> int:
        def evaluate(x, y, operator):
            if operator == "+":
                return x
            if operator == "-":
                return -x
            if operator == "*":
                return x * y
            return int(x / y)

        stack = []
        curr = 0
        previous_operator = "+"
        s += "@"

        for c in s:
            if c.isdigit():
                curr = curr * 10 + int(c)
            elif c == "(":
                stack.append(previous_operator)
                previous_operator = "+"
            else:
                if previous_operator in "*/":
                    stack.append(evaluate(stack.pop(), curr, previous_operator))
                else:
                    stack.append(evaluate(curr, 0, previous_operator))

                curr = 0
                previous_operator = c
                if c == ")":
                    while type(stack[-1]) == int:
                        curr += stack.pop()
                    previous_operator = stack.pop()

        return sum(stack)
