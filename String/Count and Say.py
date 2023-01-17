# Nested iterations, no need to do recursion.
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(n - 1):
            count = 1
            tmp = []
            for k in range(len(s)):
                if k > 0 and s[k] == s[k-1]:
                    count += 1
                if k == len(s) - 1 or s[k] != s[k+1]:
                    tmp.append(str(count))
                    tmp.append(str(s[k]))
                    count = 1
            s = str(''.join(tmp))

        return s
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n < 1:
#             return ""
#
#         tmp = []
#         s = "1"
#         for i in range(n - 1):  # Total run is n times. But the first run is already done by setting s = "1"
#             count = 1
#             for j in range(len(s)):
#                 if j + 1 < len(s) and s[j] == s[j + 1]:
#                     count += 1
#                 else:
#                     tmp.append(str(count))
#                     tmp.append(s[j])
#                     count = 1  # reset count
#             s = "".join(tmp)
#             tmp.clear()
#
#         return s

