# Just iterate through the string and count how many times #right > #left
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        left_bracket_count = 0
        for c in s:
            if c == '(':
                left_bracket_count += 1
            elif c == ')':
                left_bracket_count -= 1
                if left_bracket_count < 0:
                    res += 1
                    left_bracket_count = 0
        return res + left_bracket_count
