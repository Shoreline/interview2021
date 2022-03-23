class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)

        odd_vals = 0
        for c in counter.values():
            if c % 2 == 1:
                odd_vals += 1
                if odd_vals > 1:
                    return False

        return True
