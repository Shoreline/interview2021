# T & S: O(logN)
# If using cycle detection method in linked list we can get O(1) space
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)

            tmp = 0
            while n != 0:
                tmp += (n % 10) ** 2
                n //= 10
            n = tmp

        return n == 1
