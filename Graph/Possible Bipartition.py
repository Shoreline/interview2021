class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, node_color):
            color[node] = node_color
            for neighbor in adj[node]:
                if color[neighbor] == color[node]: return False
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - node_color):
                        return False

            return True

        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1)  # 0 stands for red and 1 stands for blue.
        for i in range(1, n + 1):
            if color[i] == -1:
                # For each pending component, run DFS.
                if not dfs(i, 0):
                    # Return false, if there is conflict in the component.
                    return False

        return True


# Typical union find, but when union, add an if statement to check if parent of dislike node is same as parent of current node.
class UF:
    def __init__(self, n):
        self.p = [i for i in range(n + 1)]

    def find(self, i):  # Find parent
        if i != self.p[i]:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, j, parent_dislike_i, parent_i):
        p_j = self.find(j)
        self.p[p_j] = parent_dislike_i
        return p_j != parent_i  # Check if there is a parent conflict


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)  # Create graph and initilize union find
        uf = UF(N)
        for (u, v) in dislikes:
            self.graph[u].append(v)
            self.graph[v].append(u)

        for i in range(1, N + 1):
            parent_i = uf.find(i)
            if parent_i in self.graph:
                parent_dislike_i = uf.find(
                    self.graph[i][0])  # Pick a dislike node's parent as a common parent for the rest of dislike nodes
                for dis in self.graph[i][1:]:  # For each dislike node
                    if not uf.union(dis, parent_dislike_i,
                                    parent_i): return False  # Return False if there is a conflict when grouping
        return True


class Solution_dfs2:
    def dfs(self, i, group):
        if i in self.group_mapping and group != self.group_mapping[i]:  # Check if there is a conflict
            return False  # between given group and existing group
        self.group_mapping[i] = group
        if i not in self.visited:
            self.visited.add(i)
            for dis in self.graph[i]:  # DFS for each dislike node recursively
                if not self.dfs(dis, not group): return False  # Assign contrary group to dislike node
        return True

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        self.visited, self.group_mapping = set(), {}
        for (u, v) in dislikes:  # Create graph
            self.graph[u].append(v)
            self.graph[v].append(u)

        for i in range(1, N + 1):  # DFS until eror
            if i not in self.visited:  # We don't want to revisit since it's DFS
                if not self.dfs(i, True):  # If conflict occurs during DFS, return False
                    return False
        return True