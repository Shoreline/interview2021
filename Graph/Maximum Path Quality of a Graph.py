def maximalPathQuality(self, A, edges, maxTime):
    G = collections.defaultdict(dict)
    for i, j, t in edges:
        G[i][j] = G[j][i] = t

    def dfs(i, seen, time):
        res = sum(A[j] for j in seen) if i == 0 else 0
        for j in G[i]:
            if time >= G[i][j]:
                res = max(res, dfs(j, seen | {j}, time - G[i][j]))
        return res

    return dfs(0, {0}, maxTime)