class UnionFind:
    def __init__(self, N):
        # self.parent = [i for i in range(N)]
        self.parent = list(range(N))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False  # already in the same cluster

        self.parent[pu] = pv

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)

        res = set()
        for i in range(n):
            res.add(uf.find(i))

        return len(res)
