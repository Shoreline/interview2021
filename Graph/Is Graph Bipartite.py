# undirected graph with n nodes, where each node is numbered between 0 and n - 1

# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the
# graph connects a node in set A and a node in set B.

# Coloring by DFS

# Color a node blue if it is part of the first set, else red. We should be able to greedily color the graph if and
# only if it is bipartite: one node being blue implies all it's neighbors are red, all those neighbors are blue,
# and so on.
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}  # also served as visited set
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            # color[nei] = color[node] ^ 1
                            color[nei] = int(not color[node])

                        elif color[nei] == color[node]:
                            return False
        return True
