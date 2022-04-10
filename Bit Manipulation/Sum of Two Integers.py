# Break + (or -) into bit operations for each bit; also compute carry/borrow
# Continue to + or - with the carry/borrow until new carry/borrow is 0

# 1) +
#   - XOR has same bit output as the + operation at each bit: 1 + 1 = 0 (and carry = 1); 1 + 0 / 0 + 1 = 1; 0 + 0 = 0
#   - Need to compute carry for every bit. Simply, all the carrys can be done by using x & y (only two 1s lead to carry bit = 1)
#       - Do (x & y) << 1 since carry is always added to a higher bit
#   -> x + y = x ^ y + ((x & y) << 1)
#   keep doing it until there no carry at all

# 2) -
#   - Still, XOR has same bit output as minus operation: 1 - 1 = 0; 1 - 0 = 1; 0 - 1 = 1 (and borrow = 1); 0 - 0 = 0
#   - Now need to handle the borrow -> ((~x) & y) <<1

# T/S: O(1) because each integer always has 32 bits.
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)

        # abs(a) >= abs(b) -->
        # a determines the sign
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y > 0:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            # difference of two integers x - y
            # where x > y
            while y > 0:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign