# There are limited strobogrammatic pairs:
#   ("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")
# To expand an existing strobogrammatic number, attach the numbers in each stro-pair to head and tail
# Note that in the end a strobogrammatic number can't start with 0 or end with 0, unless
# the number itself is just 0
#
# 3 base cases!
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        # The helper function is almost the same as findStrobogrammatic(), but doesn't
        # check for invalid cases of "0"
        def helper(n):
            # 3 base cases
            if n == 0:
                return []
            if n == 1:
                return ['0', '1', '8']
            if n == 2:
                return ['00', '11', '88', '69', '96']

            res = []
            for stro_num in helper(n - 2):
                res.append('0' + stro_num + '0')
                res.append('1' + stro_num + '1')
                res.append('8' + stro_num + '8')
                res.append('6' + stro_num + '9')
                res.append('9' + stro_num + '6')

            return res

        # Just filter out the numbers starting/ending with 0
        # s_num = 0 is a corner case
        res = []
        for s_num in helper(n):
            if s_num[0] == '0' and s_num != '0':
                continue
            else:
                res.append(s_num)

        return res
