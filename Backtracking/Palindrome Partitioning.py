# Backtracking
# T: O(n * 2^n). n is the string length.
# Keep cutting pieces from the input string, make sure each piece is a palindrome. If not palindrome drop that piece; if true continue cutting.
# For each character in the string we have 2 choices to create new palindrom substrings, one is to join with previous substring (for(...end++)) and another is to start a new palindrom substring (dfs(..end+1..)). Thus in the worst case there are 2^N palindrom substrings. Each substring will take O(N) time to check if it's palindrom and O(N) time to generate substring from start to end indexes.

# S: O(n). At most n layers of recursions

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def cut(start, tmp):
            if start == len(s):
                res.append(tmp[:])
                return

            for i in range(start+1, len(s)+1):
                piece = s[start:i]
                if piece == piece[::-1]:
                    tmp.append(piece)
                    cut(i, tmp)
                    tmp.pop()
        
        res = []
        cut(0, [])
        return res

# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []

#         def dfs(pos: int, tmp: list[str]):
#             if pos >= len(s):
#                 res.append(tmp[:])
#                 return

#             for i in range(pos, len(s)):
#                 substring = s[pos:i + 1]
#                 if substring == substring[::-1]:  # This substring is a palindrome
#                     tmp.append(substring)
#                     dfs(i + 1, tmp)
#                     tmp.pop()

#         dfs(0, [])
#         return res

# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = [] # [ [seg1, seg2, ...], [], ...] way of partitions of s.
#         self.dfs(s, [], res)
#         return res

#     def dfs(self, s, tmp, res):
#         if not s:
#             res.append(tmp)
#             return
#         for i in range(1, len(s)+1):
#             if self.isPal(s[:i]): # if the first half of s is palindrome
#                 self.dfs(s[i:], tmp+[s[:i]], res) # value of tmp itself is not changed

#     def isPal(self, s):
#         return s == s[::-1]
