# Binary divide.
# time: O(logN)
# Pow(x, -n) = Pow( 1/x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = abs(n)

        half = self.myPow(x, n // 2)

        return half * half if n % 2 == 0 else half * half * x
