# Recursion with a static pos pointer!
# Each segment starts with a number
# digit and '[' always come in a pair

# The starting pos of helper() always is 0 or an index after '['
# helper() handles everying in side a pair of '[]' (including other nested [], if there is any)
# So, helper() needs to deal with ...abc3[def]ghi]....

class Solution:
    def decodeString(self, s: str) -> str:
        pos = 0

        # For a "num[xxxx]" piece, return the decoded string
        def decodeSegment() -> str:
            nonlocal pos
            res = ''
            while pos < len(s):
                if s[pos].isdigit():  #
                    # Get the number
                    num_str = ''
                    while s[pos].isdigit():
                        num_str += s[pos]
                        pos += 1
                    pos += 1  # the first char after digit must be '['. Skip it.
                    seg = decodeSegment()

                    for i in range(int(num_str)):
                        res += seg
                elif s[pos] in 'abcdefghijklmnopqrestuvwxyz':
                    res += s[pos]
                    pos += 1
                else:  # s[pos] == ']'
                    pos += 1  # the first char after a seg must be ']'. Skip it too.
                    return res

            return res

        return decodeSegment()

# class Solution:
#     def decodeString(self, s: str) -> str:
#         pos = 0
#         def decodeSegment() -> str:
#             nonlocal pos
#             if pos > len(s):
#                 return ''

#             res = ''
#             while pos < len(s):
#                 if not s[pos].isdigit() and s[pos] != ']':
#                     res += s[pos]
#                     pos += 1
#                 elif s[pos] == ']':
#                     break
#                 else: # seeing a digit, meaning there is another segment to decode
#                     num_str = ''
#                     while pos < len(s) and s[pos].isdigit():
#                         num_str += s[pos]
#                         pos+=1
#                     pos +=1 # the first char after digit must be '['. Skip it.
#                     seg = decodeSegment()
#                     pos += 1 # skipe the ']'
#                     for i in range(int(num_str)):
#                         res += seg
#             return res

#         return decodeSegment()


# class Solution:
#     def decodeString(self, s: str) -> str:
#         return self.helper(s, [0])

#     def helper(self, s: str, pos: List[int]) -> str:
#         ans = ''
#         if pos[0] >= len(s):
#             return ''

#         while pos[0] < len(s) and s[pos[0]] != ']':
#             if not s[pos[0]].isdigit():
#                 ans += s[pos[0]]
#                 pos[0] += 1
#             else:                # when there is a digit, there is a nested [...]. This else handles this num[] block
#                 num = 0
#                 while pos[0] < len(s) and s[pos[0]].isdigit():
#                     num *= 10
#                     num += int(s[pos[0]])
#                     pos[0] += 1
#                 pos[0] += 1 # skip the '[', which always follows the number
#                 substring = self.helper(s, pos)
#                 pos[0] += 1 # skip the ']'
#                 for i in range(num):
#                     ans += substring

#         return ans