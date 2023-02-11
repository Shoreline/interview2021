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


# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         N = len(s)
#         for i in range(N // 2):
#             s[i], s[N - 1 - i] = s[N - 1 - i],s[i]
#
#         return

# Pythonic one-line solution
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s.reverse()