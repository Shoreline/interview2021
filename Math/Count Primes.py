# Mark the multiples of a prime number as non-prime. Start with the smallest prime number (which is 2)

# Optimized by some math algo
#   - The prime-multipling loop will start at 2 and go up to sqrt(n)
#   - The marking loop starats from i*i and ends at n
#   - No need to go beyond sqrt(n) because every multiple of sqrt(n) have already been addressed by k * n' where n' < sqrt(n)
# Time: O(sqrt(n)*loglogn)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(sqrt(n)) + 1):  # !
            if primes[i]:
                for j in range(i * i, n, i):  # !
                    primes[j] = False
        return sum(primes)

    # class Solution:
#     def countPrimes(self, n: int) -> int:
#         res = 0

#         primes = [True] * n
#         for i in range(2, n):
#             if primes[i]:
#                 res += 1

#                 j = i
#                 while j < n:
#                     primes[j] = False
#                     j += i

#         return res
