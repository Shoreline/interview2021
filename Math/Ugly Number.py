# Just keep dividing 2, 3, 5. If the final remainder is 1 then it is an ugly number.
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for x in [2, 3, 5]:
            while n % x == 0:
                n = n / x
        return n == 1