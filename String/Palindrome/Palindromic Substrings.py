# Palindromic questions thought: check all possible centers, instead of each characters in the string
# Every time we successfully expand a p-string, a new p-string is generated.
# T: O(n^2); S: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromes(left: int, right: int) -> int:
            p_count = 0
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    return p_count
                p_count += 1
                left -= 1
                right += 1
            return p_count

        res = 0
        for i in range(len(s)):
            res += countPalindromes(i, i)
            res += countPalindromes(i - 1, i)
        return res

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         p_count = 0
#         def findPalindromes(left:int, right:int):
#             nonlocal p_count
#             while left>=0 and right < len(s):
#                 if s[left] != s[right]:
#                     return
#                 p_count += 1
#                 left -= 1
#                 right += 1
#             return

#         for i in range(len(s)):
#             findPalindromes(i,i)
#             findPalindromes(i-1,i)
#         return p_count

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         count = [0]
#         for i in range(len(s)):
#             self.isPalindrome(s, i,i, count)
#             if i > 0:
#                 self.isPalindrome(s, i-1, i, count)

#         return count[0]

#     def isPalindrome(self, s:str, left:int, right:int, count:List[int]) -> None:
#         a= s[left]
#         b= s[right]
#         while left >= 0 and right < len(s):
#             if s[left] == s[right]:
#                 count[0] += 1
#             else:
#                 break
#             left -= 1
#             right += 1
#         return