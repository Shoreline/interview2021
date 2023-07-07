# Similar to Add Strings. Just % 2 and // 2.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = a
        num2 = b
        res = []  # a list of integer

        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            sum = x1 + x2 + carry
            value = sum % 2
            carry = sum // 2
            res.append(str(value))
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(str(carry))

        # reverse res, convert each element into string and join together
        return ''.join(res[::-1])

# Note: can't use
#   carry = sum % 2
#   res.append(sum//2)
# to handle sum and carry!
class Solution2:
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