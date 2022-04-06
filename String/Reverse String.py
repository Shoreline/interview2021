class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        k = 0
        while i + k < j - k:
            s[i + k], s[j - k] = s[j - k], s[i + k]
            k += 1

        return

# Pythonic one-line solution
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s.reverse()