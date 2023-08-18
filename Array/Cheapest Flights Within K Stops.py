# bellman-ford algo
# T: O(k*E)
# S:O(V)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = collections.defaultdict(lambda: math.inf)

        cost[src] = 0
        for _ in range(k + 1):
            cost_ = cost.copy()
            for a, b, c in flights:  # check all flights if there is a cheaper way to get b (from a)
                if cost_[b] > cost[a] + c:
                    cost_[b] = cost[a] + c
            cost = cost_

        return cost[dst] if cost[dst] != math.inf else -1


# Dijkstra (dike·struh) algorithm
# Time complexity: O(N + E*K*log(E*K))
# Space complexity: O(N + E * K)
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)  # flights map<start_city, list[(dest_city, cost)]>
        for u, v, w in flights:
            graph[u].append([v, w])

        # heap of rountes
        #   heap: (current_total_price, start, remaining_stops)
        heap = [(0, src, k + 1)]
        city_least_stops = {}

        while heap:
            p, city, s = heapq.heappop(heap)
            if city == dst:
                return p

            # We have seen another path to this city with a lower cost and fewer stops
            #   - why previous path costs less? Since the heap ranks paths by total_price and city has been seen
            if city in city_least_stops and city_least_stops[city] >= s:
                continue
            city_least_stops[city] = s

            if s:
                for dest_city, cost in graph[city]:
                    heapq.heappush(heap, (p + cost, dest_city, s - 1))
        return -1