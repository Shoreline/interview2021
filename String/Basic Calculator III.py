class Solution:
    def calculate(self, s: str) -> int:
        num, stack, sign = 0, [], "+"
        s += 'E'    # final wrap up when i == len(s)-1
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '(':
                num, skip = self.calculate(s[i+1:])
                i += skip
            elif s[i] in '+-*/)' or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                if s[i] == ')':
                    return sum(stack), i + 1
                num = 0
                sign = s[i]
            i += 1
        return sum(stack)