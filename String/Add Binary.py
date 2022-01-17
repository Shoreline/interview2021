# Note: can't use
#   carry = sum % 2
#   res.append(sum//2)
# to handle sum and carry!
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Ensure a is the longer string
        if len(a) < len(b):
            a, b = b, a

        i = 0
        carry = 0
        res = []  # reversed
        while i < len(b):
            # start from the lowest bit (rightmost bit)
            sum = carry + int(a[len(a) - 1 - i]) + int(b[len(b) - 1 - i])
            carry = 0 if sum < 2 else 1
            val = sum - carry * 2
            res.append(str(val))
            i += 1

        while i < len(a):
            sum = carry + int(a[len(a) - 1 - i])
            carry = 0 if sum < 2 else 1
            val = sum - carry * 2
            res.append(str(val))
            i += 1

        if carry > 0:
            res.append(str(carry))

        return "".join(res[::-1])  # reverse the res back