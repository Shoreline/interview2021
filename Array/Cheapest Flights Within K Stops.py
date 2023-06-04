# Dijkstra (dike·struh) algorithm
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)  # flights map<start_city, list[(dest_city, cost)]>
        for u, v, w in flights:
            graph[u].append([v, w])

        heap = [(0, src, k + 1)]  # (current_total_price, start, remaining_stops)
        city_least_stops = {}

        while heap:
            p, city, s = heapq.heappop(heap)
            if city == dst:
                return p

            if city in city_least_stops and city_least_stops[city] >= s:
                continue
            city_least_stops[city] = s

            if s:
                for dest_city, cost in graph[city]:
                    heapq.heappush(heap, (p + cost, dest_city, s - 1))
        return -1