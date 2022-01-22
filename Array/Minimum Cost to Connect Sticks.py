# Always pick two of the smallest sticks to connect and continue doing this until you get only one stick
# T: nlogn, S: 1
import heapq as hq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0

        while len(sticks) >= 2:
            first_min = heapq.heappop(sticks)
            second_min = heapq.heappop(sticks)

            cost += first_min + second_min
            heapq.heappush(sticks, first_min + second_min)

        return cost

# import heapq as hq
# class Solution:
#     def connectSticks(self, sticks: List[int]) -> int:
#         heapq.heapify(sticks)
#         cost = 0
#         first_min = heapq.heappop(sticks)

#         while sticks:
#             second_min = heapq.heappop(sticks)
#             cost += first_min + second_min

#             heapq.heappush(sticks, first_min + second_min)
#             first_min = heapq.heappop(sticks)

#         return cost