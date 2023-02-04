# The result is always like s = '0'*i + '1'*j
# The problem becomes where is the first '1' (or where is the last '0') after flipping.
#   After the last '0', all remaining chars must be '1'
#   So for every char, keep tracking the '1's before it (including itself), and '0's after it.
#   To make it the last '0', we need to flip all '1's before, and all '0's after.
#   The sum will be the cost to make this char the last '0'.
#
# Corner case: if input s is all '0'

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # cnt1: including s[i], how many '1's from beginning of the string
        # cnt0: after s[i], how many '0's to the end of the string
        # Initially, there is 0 '1's before, and all '0's in s after
        cnt1, cnt0 = 0, s.count('0')

        # Worst case, flip all '1's to '0' or the other way around
        res = min(cnt0, len(s) - cnt0)

        for c in s:
            if c == '0':
                cnt0 -= 1
            else:
                cnt1 += 1
            res = min(res, cnt0 + cnt1)
        return res

    # thought 2:
# The result is always like s = '0'*i + '1'*j
# 2 scans for s, one from the start, one from the end
# count how many 1s is before each s[i] and how many 0s after s[i]
# So we can tell for each s[i], the flipping cost to make it the boundary between 0s and 1s.