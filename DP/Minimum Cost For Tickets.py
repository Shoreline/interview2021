# dp[i]: min cost after i days
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set =set(days)

        # Create a table of all the day cost
        # * Instead of creating a 365 days table, we create until the last day on the days list
        dp = [0] * (days[-1] + 1)

        for i in range(0, days[-1] + 1):
            # We use the cost of previous day if there is no travel today.
            if i not in days_set:
                dp[i] = dp[i - 1]
            else:
                # We select the min cost for 3 cases in travel day:
                # 1. the accumulated cost in 1-day ago + the cost of 1-day pass;
                # 2. the accumulated cost in 7-day ago + the cost of 7-day pass;
                # 3. the accumulated cost in 30-day ago + the cost of 30-day pass.
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],  # per days value
                    dp[max(0, i - 7)] + costs[1],  # per week value
                    dp[max(0, i - 30)] + costs[2]  # per year value
                )

        return dp[-1]


class Solution2:
    # time: O(len(days)), space: O(31).
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Create a table of 31 days' cost
        dp = [0] * 31  # 优化：因为票期最长30天，故只需记录31天的空间。
        for i in range(0, days[-1] + 1):  # traverse each day
            if i not in set(days):  # We use the cost of previous day if there is no travel today.
                dp[i % 30] = dp[(i - 1) % 30]
            else:  # We select the min cost for 3 cases in travel day:
                # 1. the accumulated cost in 1-day ago + the cost of 1-day pass;
                # 2. the accumulated cost in 7-day ago + the cost of 7-day pass;
                # 3. the accumulated cost in 30-day ago + the cost of 30-day pass.
                dp[i % 30] = min(dp[max(0, i - 1) % 30] + costs[0],
                                    dp[max(0, i - 7) % 30] + costs[1],
                                    dp[max(0, i - 30) % 30] + costs[2])
        return dp[days[-1] % 30]  # return the cost of last day
