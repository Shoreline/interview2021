# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# PS: node values are unique
#
# Basically, build a graph based on the given tree, find the target node, then do BFS.
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # <Node_val, list<adjacent_Node_val>> -> note that we're told that node_val is unique
        # parent/child doesn't matter
        graph = collections.defaultdict(list)

        def connect(parent, child):
            # both parent and child are not empty
            if parent and child:
                # building an undirected graph representation, assign the
                # child value for the parent as the key and vice versa
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            # in-order traversal
            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)

        # the initial parent node of the root is None
        connect(None, root)

        # Do BFS for the graph, starting from the target node, hence the starting level is 0
        bfs = [target.val]
        seen = set(bfs)
        # all nodes at (k-1)th level must also be K steps away from the target node
        for i in range(k):
            # expand the list comprehension to strip away the complexity
            new_level = []
            for node_val in bfs:
                for adjacent_node_val in graph[node_val]:
                    if adjacent_node_val not in seen:
                        new_level.append(adjacent_node_val)
                        seen.add(adjacent_node_val)
            bfs = new_level
            # add all the values in bfs into seen
            # seen |= set(bfs)

        return bfs