"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# This is not a tree clone, but a graph. The problem for a graph is that it can has a cycle.
# So we have to avoid endlessly going around in a cycle.
#
# Build a map<original_node, new_node>, simple, great for cloning problems.
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        # dfs() deepcopies ALL subgraph originating from the input node
        def dfs(node):
            mapping[node] = Node(node.val)  # creates a new node and connects it with the original node
            for n in node.neighbors:
                if n not in mapping:
                    dfs(n)  # DFS copy each unseen node
                mapping[node].neighbors += [mapping[n]]

        if not node:
            return node
        mapping = {}
        dfs(node)
        return mapping[node]

# Wrong solution
# "visited" can only help us tell which node has been touched, but not enough to in copying a graph.
# This is becasue in addtional to nodes, a graph has edge information!
# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         visited = set()

#         def dfs(node:Node) -> Node:
#             if not node:
#                 return None

#             new_node = Node(node.val)
#             for n in node.neighbors:
#                 if n not in visited:
#                     visited.add(n)
#                     new_node.neighbors.append(dfs(n))

#             return new_node

#         haha =  dfs(node)

#         return haha
