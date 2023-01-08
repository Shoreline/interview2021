# Mark the multiples of a prime number as non-prime. Start with the smallest prime number (which is 2)
# Note that 0 and 1 is not prime. 2 is the first prime number.

# Optimized by some math algo
#   - The prime-multiplying loop will start at 2 and go up to sqrt(n)
#   - The marking loop starts from i*i and ends at n
#        the unique factorization theorem or the unique prime factorization theorem, states that every integer greater
#        than 1 either is a prime number itself or can be represented as the product of prime numbers. So the prime
#        numbers smaller than i would have already covered the multiples smaller than i*i
#        e.g. 7 * 2, 7 * 3, ..., 7 *6 all of these have been computed while working on 2, 3, and 5 (previous prime
#        numbers). So we only need to start from 7 * 7
#   - No need to go beyond sqrt(n) because every multiple of sqrt(n) have already been addressed by k * n' where
#       n' < sqrt(n)
# Time: O(sqrt(n)*loglogn)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        i = 2
        while i < sqrt(n):
            if primes[i]:
                for j in range(i * i, n, i):  # !
                    primes[j] = False
            i += 1
        return sum(primes)

# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n < 3:
#             return 0
#         primes = [True] * n
#         primes[0] = primes[1] = False
#         for i in range(2, int(sqrt(n)) + 1):  # !
#             if primes[i]:
#                 for j in range(i * i, n, i):  # !
#                     primes[j] = False
#         return sum(primes)

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
