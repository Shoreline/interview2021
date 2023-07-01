# PS: s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# Note that there won't be any parenthesis
# Since * and / has higher priority, sometimes we need to hold current result for the completion of later operations. Therefore, use two temp variables of cur_val and pre_val.
class Solution:
    def calculate(self, s: str) -> int:
        cur_val, pre_val, res = 0, 0, 0
        sign = '+'  # previous sign

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                cur_val = cur_val * 10 + int(c)
            if c in '+-*/' or i == len(s) - 1:
                # If previous sign is * or /, we cannot update res yet. since the next operand may need to divide/multiply its value
                if sign == '*':
                    pre_val *= cur_val
                elif sign == '/':
                    pre_val = int(pre_val / cur_val)
                # if previous sign is the low priority + or -, then the task of pre_val is done. Furture cur_val won't
                # need to consider it, so we can just update res with pre_val
                elif sign in '+-':
                    res += pre_val
                    pre_val = cur_val if sign == '+' else -cur_val

                # reset cur_val and sign after every computation
                cur_val = 0
                sign = c

        res += pre_val
        return res