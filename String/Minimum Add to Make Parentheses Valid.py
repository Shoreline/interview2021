# Just iterate through the string and count how many times #right > #left
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        moves = 0
        unmatched_left_parens = 0
        for c in s:
            if c == '(':
                unmatched_left_parens += 1
            elif c == ')':
                unmatched_left_parens -= 1
                if unmatched_left_parens < 0:
                    moves += 1
                    unmatched_left_parens = 0
        return moves + unmatched_left_parens
