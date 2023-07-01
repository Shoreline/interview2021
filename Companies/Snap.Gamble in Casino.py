# Starting money: s
# win rate: p
# bet: b
# target$: t
# play at most N rounds
#
# You either win or lose in each round
from functools import lru_cache


def get_max_win_rate(start, target, rounds, p):
    #
    @lru_cache(None)
    def helper(fund, remaining_rounds):
        if fund >= target:
            return 1
        elif remaining_rounds == 0:
            return 0
        max_win_rate = 0
        for bet in range(fund + 1):
            win_rate = p * helper(fund + bet, remaining_rounds - 1) + (1 - p) * helper(fund - bet, remaining_rounds - 1)
            max_win_rate = max(max_win_rate, win_rate)

        return max_win_rate

    return helper(start, rounds)

# print(get_max_win_rate(1, 2, 1, 0.6))
# print(get_max_win_rate(2, 3, 1, 0.6))
# print(get_max_win_rate(3, 4, 2, 0.6))
# print(get_max_win_rate(10, 20, 10, 0.6))

#def move(nums):
#     res = [0] * len(nums)
#     for i, num in enumerate(nums):
#         res[nums[nums[i]-1] - 1] = num
#
#     return res
#
# nums = [4,2,1,5,3]
# # 3, 2, 5, 1, 4
# print(move(nums))