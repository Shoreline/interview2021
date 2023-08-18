# undirected graph with n nodes, where each node is numbered between 0 and n - 1

# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the
# graph connects a node in set A and a node in set B.

# Coloring by DFS

# Color a node blue if it is part of the first set, else red. We should be able to greedily color the graph if and
# only if it is bipartite: one node being blue implies all it's neighbors are red, all those neighbors are blue,
# and so on.
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = {}  # also served as visited set
        for node in range(len(graph)):
            if node not in colored:
                stack = [node]  # used for DFS traverse. Save nodes of the current path.
                colored[node] = 0
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if neighbor not in colored:
                            stack.append(neighbor)
                            # color[nei] = color[node] ^ 1
                            colored[neighbor] = int(not colored[node])

                        elif colored[neighbor] == colored[node]:
                            return False
        return True
