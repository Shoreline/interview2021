# Can take unlimited number of courses at the same time.

# Topological sort
# 
# T & S: O(M + N) N is the number of courses; M is the number of edges
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        in_degrees = [0] * n
        for pre, nxt in relations:
            # convert into zero-based index
            # for the sake of using time[] later
            pre, nxt = pre - 1, nxt - 1

            graph[pre].append(nxt)
            in_degrees[nxt] += 1

        takeable = deque([])
        # total_time[u] is the total number of months required to finish course u
        # total_time[u] is calculated as maximum total_time of the predecessor nodes + times[u].
        total_time = time[:]
        for u in range(n):
            if in_degrees[u] == 0:
                takeable.append(u)

        while takeable:
            u = takeable.popleft()
            for v in graph[u]:
                # Update `total_time[v]` using the maximum total_time of the predecessor nodes
                # Note that u's total_time is already computed at this moment. We are updating the total_time of its
                # downstream courses.
                total_time[v] = max(total_time[u] + time[v], total_time[v])
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    takeable.append(v)

        return max(total_time)
