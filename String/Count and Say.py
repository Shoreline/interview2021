# Nested iterations, no need to do recursion.
from functools import lru_cache


class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(n - 1):  # Total run is n times. But the first run is already done by setting s = "1"
            count = 1
            tmp = []
            for k in range(len(s)):
                if k > 0 and s[k] == s[k - 1]:
                    count += 1
                if k == len(s) - 1 or s[k] != s[k + 1]:
                    tmp.append(str(count))
                    tmp.append(str(s[k]))
                    count = 1
            s = str(''.join(tmp))

        return s


def reverse_count_say(num):
    original = ''
    num = str(num)
    for i in range(0, len(num), 2):
        a, b = num[i], num[i + 1]
        current = int(a) * b
        original += current
    return original


from collections import defaultdict


def reverseCountSay(s):
    memo = defaultdict(list)  # <num_string, list<num_str>>

    # @lru_cache(None)
    def helper(s):
        if len(s) == 0:
            return [[]]
        elif s in memo:
            return memo[s]
        for i in range(1, len(s)):
            num_str, count = s[i], int(s[:i])
            for remaining_results in helper(s[i + 1:]):
                memo[s].append([num_str * count] + remaining_results)
        return memo[s]

    helper(s)
    return [''.join(output) for output in memo[s]]


print(reverseCountSay('3754'))
