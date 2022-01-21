# O(Sqrt(n)) time, O(min(k, sqrt(n))) space
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors = []  # The first half of divisors that <= sqrt_n
        sqrt_n = int(sqrt(n))

        for d in range(1, sqrt_n + 1):
            if n % d == 0:
                k -= 1
                divisors.append(d)
                if k == 0:
                    return d

        # If n is a perfect square (4, 9, 16, 25, 36, etc)
        # we have to increment k to avoid double counting
        if (sqrt_n * sqrt_n == n):
            k += 1

        # If reaching here, it means the result factor is > sqrt_n
        # We know that res * some_guy_in_divisors == n
        return n // divisors[len(divisors) - k] if len(divisors) - k >= 0 else -1