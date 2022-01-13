# Math. Decompose both input numbers, multiply one by one, and sum them up.
#   23
# * 45
# ------
#   15  5*3
#  12   4*3
#  10   5*2
# +8    4*2
# -----
# 1035
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = [0] * (len(num1) + len(num2))  # basic math, the product's length is at most len1+len2
        pos = len(product) - 1  # start from the right-hand side

        # Iterate each digit-digit pairs in num1 and num2
        for d1 in reversed(num1):
            tmp_pos = pos
            for d2 in reversed(num2):
                product[tmp_pos] += int(d1) * int(d2)
                product[tmp_pos - 1] += product[tmp_pos] // 10
                product[tmp_pos] %= 10
                tmp_pos -= 1
            pos -= 1

        # count possible zeros at the beginning, then return a string based on the product[] array
        pt = 0
        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))
