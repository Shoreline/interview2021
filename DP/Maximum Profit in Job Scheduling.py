# copied
# Sort the jobs by endTime.
# DP array is a list, not a fixed size array.
# dp[[job_time, max_profit]] means that by the end of "job_time", we can make at most "max_profit"
# Initial dp[0] = 0, as we make profit = 0 at time = 0.

# For each job = [s, e, p], where s,e,p are its start time, end time and profit,
# Then the logic is similar to the knapsack problem.
# If we don't do this job, nothing will be changed.
# If we do this job, binary search in the dp to find the largest profit we can make before start time s.
# So we also know the maximum current profit that we can make doing this job.

# Then compare with last element in the dp, if we make more money,
#   -> it is worth doing this job, and we add the pair of [e, cur] to the back of dp.
# Otherwise, we'd like not to do this job.


# Complexity
# Time O(NlogN) for sorting
# Time O(NlogN) for binary search for each job
# Space O(N)
import bisect


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by the 2nd element (endTime)
        # jobs is a list[list[int]]
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])

        dp = [[0, 0]]  # at time 0, max_profit is 0
        for s, e, p in jobs:
            # If we do this job, then need to find i that dp[i]'s end time is same or before this job's start time
            # i = bisect.bisect_left(dp, [s + 1, float('-inf')]) - 1 # build-in binary search
            # Do -1 in the end: bisect_right gives the insertion point, so -1 is the last existing element in dp, which
            # is the one we want to use in later comparison
            i = bisect.bisect_right(dp, [s, float('inf')]) - 1

            # we know that dp[-1][0] <= e, now dp[-1][1] als < dp[i][1]+ p, so dp[] is sorted.
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]