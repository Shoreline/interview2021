# Hard part is that the reversed number may overflow.
# Use int(x/10) instead of x//10 since they are different when x is a neagtive number.
# Do do x = abs(x) since it may overflow
class Solution:
    def reverse(self, x: int) -> int:
        upper_bound = 2 ** 31 - 1  # pow(2,31) - 1
        lower_bound = -2 ** 31

        res = 0
        while x != 0:
            digit = x % 10 if x > 0 else (x % -10)  # the last digit of current x. if x < 0, digit < 0.
            x = int(x / 10)  # python's way of getting same a/b in C++

            # check bounds
            if res > upper_bound // 10 or (res == upper_bound // 10 and digit > upper_bound % 10):
                return 0
            if res < int(lower_bound / 10) or (res == int(lower_bound / 10) and digit < lower_bound % -10):
                return 0

            res = res * 10 + digit

        return res

# Only works for Python or other languages having no overflow
# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = 1 if x > 0 else -1
#         str_x = str(abs(x))
#         res =  sign*int(str_x[::-1])
#         return res if -2**31 <= res <= 2**31-1 else 0

