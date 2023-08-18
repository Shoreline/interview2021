# Approach 4: Expand Around Center
# “插位”: 2n - 1 cases to check. Even length palindrome does not center at a character!

# Try letting each s[i] to be the middle one/two character(s), then expend from the middle to see what's the maximum
# palindromic substring for that.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        # start and end are inclusive indices of the result max p-substring
        res = ""
        for i in range(len(s)):
            start, end = self.expandAroundCenter(s, i, i)

            if len(res) < end - start + 1:
                res = s[start:end + 1]

            if i + 1 < len(s) and s[i] == s[i + 1]:
                start, end = self.expandAroundCenter(s, i, i + 1)
                if len(res) < end - start + 1:
                    res = s[start:end + 1]

        return res

    # return the start and end of a p-substring that centers at the left-th and right-th char(s) of s (note,
    # not center at s[left:right]!)
    def expandAroundCenter(self, s: str, left: int, right: int) -> List[int]:
        res = [left, right]
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res = [left, right]
            left -= 1
            right += 1
        return res

# A bit faster solution, if we let expandAroundCenter to only return an integer:
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s)==1:
#             return s

#         # start and end are inclusive indice of the result max p-substring
#         start = 0
#         end = 0
#         for i in range(len(s)):
#             res = s[start:end+1]
#             len1 = self.expandAroundCenter(s, i, i)

#             # 1 + 2 * len1 is the length of current max p-substring
#             if(1 + 2 * len1 > end - start + 1): # len1+1 to include the length of character i
#                 start = i - len1
#                 end = i + len1

#             if(i+1 < len(s) and s[i]==s[i+1]):
#                 len2 = self.expandAroundCenter(s,i,i+1)
#                 if(2 + 2*len2 > end - start + 1): # len2+2 to include the length of character i and i + 1
#                     start = i - len2
#                     end = i+1 + len2

#         return s[start:end+1]

#     # [left - res_len, right + res_len] is the max p-substring.
#     def expandAroundCenter(self, s:str, left:int, right:int) -> int:
#         while left>=0 and right < len(s) and s[left] == s[right]:
#             left-=1
#             right+=1
#         return (right-left)//2 - 1

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s)==1:
#             return s

#         # start and end are inclusive indice of the result string
#         start = 0
#         end = 0
#         for i in range(len(s)):
#             len1 = self.expandAroundCenter(s, i, i)
#             len2 = self.expandAroundCenter(s,i,i+1)
#             len3 = max(len1, len2)
#             if(len3 > end - start):
#                 start = i - (len3-1)//2
#                 end = i + len3//2
#                 print(s[start:end+1])

#         return s[start:end+1]

#     def expandAroundCenter(self, s:str, left:int, right:int) -> int:
#         while left>=0 and right < len(s) and s[left] == s[right]:
#             left-=1
#             right+=1
#         return right-left-1