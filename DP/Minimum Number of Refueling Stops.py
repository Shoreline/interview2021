# dp[i]: the farthest location we can get to using i refueling stops.
#   if dp[i] >= target -> we can reach the target with i stops
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [0] * (len(stations) + 1)  # dp[0] = startFuel
        dp[0] = startFuel
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):  # check current and all previous stops
                # only previous stops having enough fuel to reach the current station are qualified
                # if we can reach this station from a previous station with t refueling stops, update
                # the maximum reach of t+1 refueling stops
                if dp[t] >= location:
                    dp[t + 1] = max(dp[t + 1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target:
                return i

        return -1
