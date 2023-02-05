# Initialize a full-length product[] for simplicity
#
# Math. Decompose both input numbers, multiply one by one, and continuously sum them up.
# Note: Remove redundant 0s at the beginning, if there is any
#   23
# * 45
# ------
#    15  3*5
#   12   3*4
#   10   2*5
# + 8    2*4
# -----
#  1035
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = [0] * (len(num1) + len(num2))  # basic math, the product's length is at most len1+len2
        cur_round_pos = len(product) - 1  # start from the right-hand side

        # Iterate each digit-digit pairs in num1 and num2
        for d1 in reversed(num1):
            pos = cur_round_pos
            for d2 in reversed(num2):
                val = product[pos] + int(d1) * int(d2)
                product[pos] = val % 10
                product[pos - 1] += val // 10
                pos -= 1
            cur_round_pos -= 1

        # count possible zeros at the beginning, then return a string based on the product[] array
        pt = 0
        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))
