# O(Sqrt(n)) time, O(min(k, sqrt(n))) space
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors = []  # The first half of divisors that <= sqrt_n
        sqrt_n = int(sqrt(n))

        for d in range(1, sqrt_n + 1):
            # When n % d == 0, we actually found two divisors: d and n//d
            if n % d == 0:
                k -= 1
                divisors.append(d)
                if k == 0:
                    return d

        # If n is a perfect square (4, 9, 16, 25, 36, etc), then sqrt(n) and n // sqrt(n) is considered two
        # divisors -> double counted.
        # So we have to increment k by 1 to offset the double counting
        if sqrt_n * sqrt_n == n:
            k += 1

        # len(divisors) has all first half divisors. If the remaining k is bigger than the number
        # of first half divisors, then even count all 2nd half divisors we still can't reach k.
        if k > len(divisors):
            return -1
        else:
            return n // divisors[len(divisors) - k]