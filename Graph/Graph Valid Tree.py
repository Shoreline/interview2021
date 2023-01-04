# 1. Build a graph based on given edges
# 2. Traverse (DFS or BFS) the graph. If it is not acyclic, or there is unconnected nodes, then return False
# 3. Otherwise return True
#
# Can also be solved by union find
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()
        if self.has_cycle(0, -1, graph, visited):
            return False

        return len(visited) == n

    def has_cycle(self, node, parent, graph, visited):
        visited.add(node)
        for nbr in graph[node]:
            if nbr == parent:
                continue
            elif nbr in visited or self.has_cycle(nbr, node, graph, visited):
                return True

        return False
