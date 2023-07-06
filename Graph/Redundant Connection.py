# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

class UnionFind:
    def __init__(self, n):
        # <node_id, parent_node_id> map
        # Initialize this map so that each node is its own parent_node
        self.parent = [i for i in range(n)]
        # self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:  # if the parent_node of x is not itself
            # reset its parent node to be the ultimate parent (path compression)
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        # pu, pv are the parents of u and v
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False  # Return False if u and v are already union

        self.parent[pv] = pu
        #
        # if self.size[pu] > self.size[pv]: # Union by larger size
        #     self.size[pu] += self.size[pv]
        #     self.parent[pv] = pu
        # else:
        #     self.size[pv] += self.size[pu]
        #     self.parent[pu] = pv

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u - 1, v - 1):  # nodes are labled from 1 to n, not 0 to n - 1
                return [u, v]

# DFS
# O(N^2)
# class Solution2:
#     def findRedundantConnection(self, edges):
#         graph = collections.defaultdict(set)

#         # returns True if source and target are connected
#         def is_connected(source, target):
#             if source == target:
#                 return True
#             elif source not in seen:
#                 seen.add(source)
#                 #return any(dfs(nei, target) for nei in graph[source])
#                 for nei in graph[source]:
#                     if is_connected(nei, target):
#                         return True

#             return False

#         # Build the graph gradually.
#         # Check edges one by one. If there is no cycle, u and v won't be connected already.
#         for u, v in edges:
#             seen = set()
#             if u in graph and v in graph and is_connected(u, v):
#                 return u, v # returns the last edge in edges causing a cycle
#             graph[u].add(v)
#             graph[v].add(u)