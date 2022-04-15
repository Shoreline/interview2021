# copy with change
# "We can use the standard two-pointer approach that starts at the left and right of the string and move inwards. Whenever there is a mismatch, we can either exclude the character at the left or the right pointer. We then take the two remaining substrings and compare against its reversed and see if either one is a palindrome."

# t:O(n), s: O(1)
# somehow it takes longer time than the solution below, although both of them shall be O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(i + 1, j) or isPalindrome(i, j - 1)
            i += 1
            j -= 1
        return True

# t & s: O(n)
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def isPalindrome(s):
#             return s == s[::-1]
#         i,j = 0,len(s)-1
#         while i < j:
#             if s[i] != s[j]:
#                 delete_i = s[i+1:j+1]
#                 delete_j = s[i:j]
#                 return isPalindrome(delete_i) or isPalindrome(delete_j)
#             i += 1
#             j -= 1
#         return True

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         i = 0
#         j = len(s)-1
#         while i < j:
#             if s[i] != s[j]:
#                 delete_i = s[i+1:j+1]
#                 delete_j = s[i:j]
#                 return self._isPalindrome(delete_i) or self._isPalindrome(delete_j)
#             i += 1
#             j -= 1
#         return True

#     def _isPalindrome(self, s):
#         return s == s[::-1]
