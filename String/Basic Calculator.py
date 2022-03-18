# PS: s consists of digits, '+', '-', '(', ')', and ' '. (No * and /)
# Computation happens when a operand number has finished being parsed
# Repeat res += res * sign till the end.
# Stack saves number and sign.
# t&s: O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # used as a cache, for handling parenthesis. Saves result before a new found '('
        operand = 0  # number for next computation
        sign = 1  # 1 for positive, -1 for negative
        res = 0

        for c in s:
            if c.isdigit():  # the operand number is not yet completed, update it.
                operand = operand * 10 + int(c)
            elif c == '+':
                res += operand * sign
                sign = 1  # to be used in the next computation
                operand = 0  # reset operand after every computation
            elif c == '-':  # similar operations as "+"
                res += operand * sign
                sign = -1
                operand = 0
            elif c == '(':
                stack.append(res)  # cache current result
                stack.append(sign)
                sign = 1  # reset sign and res, for preparing evaluation for a new substring
                res = 0
            elif c == ')':  # similar to +/-, ) indicates the operand number has completed
                res += operand * sign  # res is just the result of this parenthesis
                res *= stack.pop()  # What's poped is the sign of this parenthesis
                res += stack.pop()  # what's poped now is the value of cached result before this parenthesis
                operand = 0
            # if c == ' ' (whitespace) then skip it

        res += operand * sign  # don't forget the last computation

        return res
