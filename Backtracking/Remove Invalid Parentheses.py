# Need to make sure there are equivalent number of '(' and ')'
#   -> There is no more ( than ); and vice versa
# First, make sure there is no more ( than ), then reverse the string to check there is no more ) than (
# The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative, we have more ‘)’ than ‘(‘ in the prefix.
#

# Copied and rewrote in python
# https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution
# Only generate valid result. So a lot faster than checking all possible removals.
# T: O(2^n)? # better than O(n!)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        self.helper(s, res, 0, 0, ['(', ')'])
        return res

    # the last removal position: If we do not have this position, we will generate duplicate by removing two ‘)’ in two steps only with a different order.
    def helper(self, s: str, res: List[str], start_pos: int, last_removal_pos: int, par: List[str]):
        cnt = 0  # counter.
        for i in range(start_pos, len(s)):
            if s[i] == par[0]:
                cnt += 1
            elif s[i] == par[1]:
                cnt -= 1

            if cnt >= 0:  # s[start_pos: i+1] is valid
                continue

            # when cnt <0, meaning par[1] is one more than par[0]. We can remove any one of the par[1] showed earlier
            # To avoid equivalent removals,we don't need to check for the whole s[:i+1], but only the piece of s[last_removal_pos, i+1]
            # This is because before last_removal_pos has been checked by previous helper() call
            for j in range(last_removal_pos, i + 1):
                # To avoid equivalent removals (when there are consecutive par[1])
                if s[j] == par[1] and (j == last_removal_pos or s[j - 1] != par[1]):
                    # remove s[j]. Now s[:i+1] is valid, but we still need to continue checking s[i+1:]
                    # But note that after dropping s[j], s is one charachter less,
                    # so old s[i+1:] becomes s[i:], therefore the next start_pos is i
                    self.helper(s[:j] + s[j + 1:], res, i, j, par)
            return

        # When reaching here, we only confirmed that there is no more par[1] than par[0]
        # But we still need to check there is also no more par[0] than par[1]. So reverse the string and call run helper again
        reversed_s = s[::-1]
        if par[0] == '(':  # if par[0] is '(' then it means we haven't checked the reversed string
            self.helper(reversed_s, res, 0, 0, [')', '('])
        else:  # else, it means we have checked and input s is already reversed, so append the revserd_s back to res
            res.append(reversed_s)
        return

# Check every possible removal, not very efficient
# T: O(N!)
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         # initialize a set with one element
#         # set is used here in order to avoid duplicate element
#         level = {s}
#         while True:
#             valid = []
#             for elem in level:
#                 if self.isValid(elem):
#                     valid.append(elem)
#             if valid:
#                 return valid
#             # initialize an empty set
#             new_level = set()
#             # BFS
#             for elem in level:
#                 for i in range(len(elem)):
#                     new_level.add(elem[:i] + elem[i + 1:])
#             level = new_level

#     def isValid(self,s):
#         count = 0
#         for c in s:
#             if c == '(':
#                 count += 1
#             elif c == ')':
#                 count -= 1
#                 if count < 0:
#                     return False
#         return count == 0        