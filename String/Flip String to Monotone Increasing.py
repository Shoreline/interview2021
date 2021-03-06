# The result is always like s = '0'*i + '1'*j
# The problem becomes where is the first '1' after flipping.
#   After the first '1', all remaining chars must be '1'
#   So for every char, keep tracking the '1's before it and '0's after it. The sum will be the cost to make this char the first '1'.
#
# Corner case: if input s is all '0'

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)

        # Initially, there is 0 '1's before, and all '0's in s after
        cnt1, cnt0 = 0, s.count('0')

        # Worst case, flipp all '1's to '0' or the other way around
        res = min(cnt0, n - cnt0)
        for i in range(n):
            if s[i] == '0':
                cnt0 -= 1
            elif s[i] == '1':
                cnt1 += 1
            res = min(res, cnt1 + cnt0)
        return res

    # thought 2:
# The result is always like s = '0'*i + '1'*j
# 2 scans for s, one from the start, one from the end
# count how many 1s is before each s[i] and how many 0s after s[i]
# So we can tell for each s[i], the flipping cost to make it the boundary between 0s and 1s.